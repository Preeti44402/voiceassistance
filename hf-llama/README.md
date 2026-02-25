---
title: Kodbank Voice Assistant
sdk: static
emoji: 🎙️
colorFrom: indigo
colorTo: slate
---

# Kodbank Voice Assistant

A completely free, serverless voice assistant powered by Hugging Face's Llama 3 model. No API keys required - just deploy and use!

## Features

- 🎤 **Voice Recognition**: Web Speech API for hands-free interaction
- 🤖 **Llama 3 Powered**: Uses Hugging Face's Meta-Llama-3-8B-Instruct model
- 🔊 **Text-to-Speech**: Natural voice responses using Web Speech Synthesis
- 🎨 **Beautiful UI**: Dark glassmorphic design with Tailwind CSS
- 🔄 **Real-time**: Instant responses with visual status indicators
- 💰 **Completely Free**: No API keys or paid services required

## Quick Start

1. Create a new Space on Hugging Face
2. Select **Static** SDK
3. Upload the `index.html` file
4. That's it! Your voice assistant is live

## How It Works

- **Speech Input**: Uses your browser's built-in speech recognition
- **AI Processing**: Queries Hugging Face's hosted Llama 3 model
- **Voice Output**: Converts responses to speech using Web Speech API
- **Visual Feedback**: Pulsating orb shows current state (Idle/Listening/Thinking/Speaking)

## Usage

1. Visit your deployed Space URL
2. Allow microphone permissions when prompted
3. Hold the "🎤 Hold to Listen" button and speak
4. The assistant will respond with both text and voice

## Pre-built Responses

- "Hi" → Friendly greeting
- "How are you?" → Polite response
- "What is your name?" → Assistant identity
- "Thank you" → Polite acknowledgment
- Any other query → Processed by Llama 3 with human-like responses

## Technical Details

- **Model**: `meta-llama/Meta-Llama-3-8B-Instruct`
- **Frontend**: Pure HTML/CSS/JS (no build required)
- **Dependencies**: 
  - Tailwind CSS (CDN)
  - Hugging Face Inference Client (CDN)
- **Browser APIs**: 
  - Web Speech Recognition
  - Web Speech Synthesis
- **API Access**: 
  - On Hugging Face Spaces: Token securely managed by platform
  - Local testing: Uses public endpoints without authentication

## Customization

You can easily modify:
- Trigger responses in the `processInput()` function
- Model parameters in the `queryLLM()` function
- UI styling using Tailwind classes
- Visual animations and colors

## Limitations

- Requires modern browser with Web Speech API support
- Internet connection needed for Llama 3 inference
- May be subject to Hugging Face's rate limits for free usage

## Security

- No sensitive data stored client-side
- On Hugging Face Spaces, API keys are securely managed by the platform
- All processing happens through secure Hugging Face endpoints
- Microphone access only when button is held
- In local testing, the app connects to public Hugging Face endpoints without requiring an API key

## Troubleshooting

- **No speech recognition?** Ensure browser supports Web Speech API
- **No audio output?** Check browser audio permissions
- **Slow responses?** May be due to Hugging Face rate limits
- **Microphone not working?** Check site permissions in browser settings