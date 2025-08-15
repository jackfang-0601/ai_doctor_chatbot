# AI Doctor Chat

## Overview

This project is an AI-powered doctor chat application that provides location-based medical consultations using OpenAI's GPT models. It supports users from the USA and China with tailored prompts, maintains conversation history, and generates summaries for real doctors.

## Features
- Country-specific AI doctor responses (USA and China).
- Session-based conversation isolation.
- Automatic summary generation to end consultations.
- Responsive web interface for user input and chat.

## Installation
1. Clone the repository.
2. Set up virtual environment: `python -m venv .venv` and activate it.
3. Install dependencies: `pip install flask python-dotenv openai`.
4. Add `OPENAI_API_KEY` to `.env`.
5. Run: `python app.py`.

## Key Files

### app.py
The main Flask application file that handles routing:
- Serves the index page.
- Starts new conversations.
- Processes chat messages.
- Manages session-based conversation IDs.

```python:%2FUsers%2Fjackfang%2FDesktop%2FAI%20Project%20%2Fapp.py
from flask import Flask, render_template, request, jsonify, session
import uuid
from hello import DoctorConversation

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Add a secret key for session management

conversations = {}

@app.route('/')
def index():
    // ... existing code ...

@app.route('/start', methods=['POST'])
def start():
    // ... existing code ...

@app.route('/chat', methods=['POST'])
def chat():
    // ... existing code ...

@app.route('/new_conversation', methods=['POST'])
def new_conversation():
    // ... existing code ...

if __name__ == '__main__':
    app.run(debug=True)
```

### hello.py
Contains the `DoctorConversation` class for OpenAI integration:
- Loads API key from environment.
- Defines country-specific prompts and guardrails.
- Manages chat logic and summary detection.

```python:%2FUsers%2Fjackfang%2FDesktop%2FAI%20Project%20%2Fhello.py
from openai import OpenAI
import openai
import os
from dotenv import load_dotenv

// ... existing code ...

class DoctorConversation:
    def __init__(self, country):
        // ... existing code ...

    def chat(self):
        // ... existing code ...

if __name__ == "__main__":
    // ... existing code ...
```

### index.html
The frontend template in `templates/` folder:
- Handles country selection, user info form, and chat UI.
- Includes JavaScript for dynamic interactions and message formatting.

```html:%2FUsers%2Fjackfang%2FDesktop%2FAI%20Project%20%2Ftemplates%2Findex.html
<!DOCTYPE html>
<html lang="en">
<head>
    // ... existing code ...
</head>
<body class="bg-gray-50 text-gray-900">
    // ... existing code ...
</body>
</html>
```

## Usage
Access `http://localhost:5000`, select country, enter info, and chat.

## Disclaimer
Not for real medical use. Consult professionals.

## License
MIT
