# AI Voice Assistant

An advanced ChatGPT-style voice assistant that listens to your voice, processes the input through an LLM (OpenAI GPT-4o-mini), and responds with text-to-speech. The assistant is designed to respond to specific triggers like saying "hi" which will result in a "hello" response, but also handles complex queries through the LLM.

## Features

- Speech Recognition using Google's Web Speech API
- LLM-powered responses using OpenAI GPT-4o-mini
- Text-to-Speech functionality
- Advanced Web interface with "Neural Glow" design
- Trigger-based responses (e.g., "hi" triggers "hello")
- Conversation logging with history
- Visual status indicators (Idle, Listening, Thinking, Speaking)
- Interruptible speaking functionality
- Responsive UI with visual feedback

## Prerequisites

- Python 3.7 or higher
- Microphone for speech input
- Speakers for speech output
- OpenAI API key for LLM functionality

## Installation

1. Clone this repository or navigate to the voice-assistant directory
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key:
   - Create a `.env` file by copying the example: `cp .env.example .env`
   - Get your OpenAI API key from [platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
   - Replace `your_openai_api_key_here` in the `.env` file with your actual API key

Note: Installing PyAudio (needed for speech recognition) can sometimes be challenging on certain systems. If you encounter issues, you might need to install it separately:

On macOS:
```bash
brew install portaudio
pip install pyaudio
```

On Ubuntu/Debian:
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
pip install pyaudio
```

On Windows, you can try:
```bash
pip install pipwin
pipwin install pyaudio
```

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Open your web browser and go to `http://localhost:5001`

3. Click the "Start Listening" button and speak into your microphone

4. The assistant will process your input and respond accordingly

## Trigger Responses

The voice assistant is programmed with specific responses for certain inputs:

- Saying "hi" or "hello" will trigger a "hello" response
- Saying "how are you" will trigger an appropriate response
- Saying "what is your name" will return the assistant's identity
- Saying "thank you" or "thanks" will respond with a polite acknowledgment
- Other inputs will be processed by the LLM for more sophisticated responses

## Architecture

- `app.py`: Main Flask application with speech recognition and text-to-speech functionality
- `templates/index.html`: Frontend interface with Tailwind CSS styling
- `requirements.txt`: Python dependencies

## Troubleshooting

- If you get a PyAudio-related error, make sure it's properly installed as described above
- If speech recognition doesn't work, ensure your microphone is properly connected and configured
- For better speech recognition accuracy, try speaking clearly in a quiet environment
- The Google Web Speech API requires an internet connection to work properly

## Limitations

- The speech recognition relies on Google's Web Speech API, which requires an internet connection
- Accuracy of speech recognition may vary depending on microphone quality and ambient noise
- The assistant currently has a limited set of trigger responses; expanding this would require modifying the `process_input` function in `app.py`

## Extending Functionality

To add more trigger responses, modify the `process_input` function in `app.py` to include additional conditional checks.