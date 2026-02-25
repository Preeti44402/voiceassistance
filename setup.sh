#!/bin/bash

echo "Setting up AI Voice Assistant..."

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "Creating .env file from example..."
    cp .env.example .env
    echo "Please edit .env to add your OpenAI API key"
else
    echo ".env file already exists"
fi

echo "Installation complete!"
echo ""
echo "To run the application:"
echo "1. Edit the .env file to add your OpenAI API key"
echo "2. Run: python app.py"
echo "3. Visit: http://localhost:5001"