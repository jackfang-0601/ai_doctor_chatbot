# AI Doctor Chat

A web-based AI medical consultation system that provides preliminary diagnosis and recommendations based on patient symptoms, with country-specific medical approaches for the US and China.

## Features

- **Country-Specific Medical Advice**: Tailored medical guidance for US and China healthcare systems
- **Patient Information Collection**: Gathers name, age, gender, and other relevant details
- **Interactive Chat Interface**: ChatGPT-style conversation with an AI doctor
- **Structured Diagnosis Summaries**: Provides organized summaries with:
  - Symptoms
  - Assessment
  - Recommendations
- **Responsive Design**: Works on desktop and mobile devices

## Technologies Used

- **Backend**: Python with Flask
- **Frontend**: HTML, CSS (Tailwind), JavaScript
- **AI**: OpenAI GPT-4 (or similar model)
- **Deployment**: Vercel (optional)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-doctor-chat.git
cd ai-doctor-chat
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your API key: `OPENAI_API_KEY=your_api_key_here`

5. Run the application:
```bash
flask run
```

## Usage

1. Open your browser to `http://localhost:5000`
2. Select your country (USA or China)
3. Enter your personal information
4. Describe your symptoms to the AI doctor
5. Receive a structured diagnosis summary

## Project Structure
# ai_doctor_chatbot
