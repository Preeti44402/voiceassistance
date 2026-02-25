import speech_recognition as sr
import pyttsx3
import threading
import json
import os
from gtts import gTTS
from flask import Flask, render_template, jsonify, request
import subprocess
from openai import OpenAI
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak_text(text):
    """Convert text to speech using system TTS or gTTS as fallback"""
    try:
        # Try to use pyttsx3 first
        engine = pyttsx3.init()
        
        # Configure voice properties
        voices = engine.getProperty('voices')
        if voices:
            engine.setProperty('voice', voices[0].id)  # Use the first available voice
        engine.setProperty('rate', 150)  # Speed of speech
        engine.setProperty('volume', 0.9)  # Volume level
        
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"pyttsx3 error: {e}")
        try:
            # Fallback to gTTS and system say command on macOS
            tts = gTTS(text=text, lang='en')
            tts.save("temp_audio.mp3")
            # Use macOS built-in say command
            subprocess.run(["say", text])
            # Clean up temp file
            if os.path.exists("temp_audio.mp3"):
                os.remove("temp_audio.mp3")
        except Exception as e2:
            print(f"gTTS fallback error: {e2}")
            # Last resort: print to console
            print(f"Response: {text}")

app = Flask(__name__)

# Removed redundant function since it's now defined above

def listen_for_speech():
    """Listen for speech from the microphone and return recognized text"""
    try:
        with microphone as source:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        
        print("Processing audio...")
        # Using Google Web Speech API
        text = recognizer.recognize_google(audio)
        return text.lower().strip()
    except sr.WaitTimeoutError:
        return "timeout_error"
    except sr.UnknownValueError:
        return "unrecognized_speech"
    except sr.RequestError as e:
        return f"api_error: {str(e)}"

def query_llm(prompt):
    """Query the OpenAI LLM with the given prompt"""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key or api_key == "your_openai_api_key_here":
        return "Please set your OpenAI API key in the .env file to enable advanced responses. For now, I can only respond to simple triggers like 'hi'."
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error querying LLM: {e}")
        return f"Sorry, I encountered an error: {str(e)}"


def process_input(text):
    """Process the recognized text and return appropriate response"""
    # Check for simple triggers first
    if text == "hi" or text == "hello":
        return "hello"
    elif "how are you" in text:
        return "I am doing well, thank you for asking!"
    elif "what is your name" in text:
        return "I am your AI voice assistant, powered by OpenAI GPT."
    elif "thank you" in text or "thanks" in text:
        return "You're welcome! Is there anything else I can help with?"
    else:
        # For more complex queries, use the LLM
        llm_response = query_llm(text)
        return llm_response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listen', methods=['POST'])
def handle_listen():
    """Endpoint to trigger speech recognition"""
    try:
        recognized_text = listen_for_speech()
        
        if recognized_text == "timeout_error":
            response_text = "I didn't hear anything. Please try again."
        elif recognized_text == "unrecognized_speech":
            response_text = "I couldn't understand what you said. Please try again."
        elif "api_error" in recognized_text:
            response_text = "There was an issue with the speech recognition service."
        else:
            response_text = process_input(recognized_text)
            
            # Speak the response in a separate thread so the API responds immediately
            speak_thread = threading.Thread(target=speak_text, args=(response_text,))
            speak_thread.start()
        
        return jsonify({
            'success': True,
            'input': recognized_text,
            'response': response_text
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/speak', methods=['POST'])
def handle_speak():
    """Endpoint to convert text to speech"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if text:
            speak_thread = threading.Thread(target=speak_text, args=(text,))
            speak_thread.start()
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    print("Starting Voice Assistant...")
    print("Visit http://localhost:5000 to use the web interface")
    app.run(debug=True, host='0.0.0.0', port=5001)