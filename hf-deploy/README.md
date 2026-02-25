---
title: AI Voice Assistant
sdk: static
emoji: 🎙️
colorFrom: indigo
colorTo: slate
---

# AI Voice Assistant for Hugging Face Spaces

An advanced ChatGPT-style voice assistant that listens to your voice, processes the input through an LLM (OpenAI GPT-4o-mini), and responds with text-to-speech. The assistant is designed to respond to specific triggers like saying "hi" which will result in a "hello" response, but also handles complex queries through the LLM.

## Features

- Speech Recognition using Web Speech API
- LLM-powered responses using OpenAI GPT-4o-mini
- Text-to-Speech functionality
- Advanced Web interface with "Neural Glow" design
- Trigger-based responses (e.g., "hi" triggers "hello")
- Conversation logging with history
- Visual status indicators (Idle, Listening, Thinking, Speaking)
- Interruptible speaking functionality
- Responsive UI with visual feedback
- Glassmorphic design with Tailwind CSS

## Prerequisites

- Microphone for speech input
- Speakers for speech output
- OpenAI API key for LLM functionality

## Deployment on Hugging Face Spaces

1. Create a new Space on Hugging Face
2. Select the **Static** SDK
3. Upload all files in this repository
4. In the Space Settings, go to "Variables and Secrets"
5. Add a new **Secret** named `OPENAI_API_KEY` with your OpenAI API key
6. The application will automatically deploy and be accessible at your Space URL

## Configuration

The application is configured to work with Hugging Face Spaces:
- Uses `window.huggingface.variables.get()` to securely access the API key
- Provides appropriate error messages when API key is not configured
- Works with the Hugging Face Spaces static SDK

## Usage

1. Once deployed, visit your Space URL
2. Allow microphone access when prompted
3. Hold the "Hold to Listen" button and speak your query
4. The assistant will process your input and respond via text-to-speech
5. View the conversation history in the log panel

## Trigger Responses

The voice assistant is programmed with specific responses for certain inputs:

- Saying "hi" or "hello" will trigger a "hello" response
- Saying "how are you" will trigger an appropriate response
- Saying "what is your name" will return the assistant's identity
- Saying "thank you" or "thanks" will respond with a polite acknowledgment
- Other inputs will be processed by the LLM for more sophisticated responses

## Troubleshooting

- If you see a message about the API key not being configured, ensure you've added it in the Space Settings under Variables and Secrets
- If speech recognition doesn't work, ensure your browser has microphone permissions
- For better speech recognition accuracy, speak clearly in a quiet environment

## Security

- API keys are stored securely as Hugging Face Space Secrets
- The API key is never exposed in the client-side code
- All API calls are made securely through the browser

## Architecture

- `index.html`: Complete frontend application with Web Speech API integration
- Secure API key handling via Hugging Face variables
- Client-side speech recognition and synthesis
- Direct integration with OpenAI API for LLM responses