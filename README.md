# Chat-bot-application
This is a chatbot web application built using Google Gemini AI LLMs and Streamlit. The app allows users to have interactive conversations powered by advanced language models, suitable for experimenting with AI responses or building as a foundation for AI assistants.

# Features
✅ Conversational AI — Engage with a chatbot powered by Gemini AI’s large language models (LLMs).
✅ Streamlit Interface — Clean, responsive, and easy-to-use web UI.
✅ Secure API Handling — API keys and sensitive data are managed via environment variables using python-dotenv.
✅ Real-time Chat — Get instant responses as you type.
✅ Lightweight & Extendable — Simple structure that can be enhanced with additional features like memory, context, or database integration.

# Tech Stack
Frontend - Streamlit
Backend - Python
AI Model - Google Gemini Generative AI (via google-generativeai library)
Config - python-dotenv

# Project Structure

├── app.py                   # Main Streamlit app
├── .env                      # API keys and secrets (DO NOT COMMIT)
├── requirements.txt          # Python dependencies

# Install dependencies
pip install -r requirements.txt

# requirements.txt
streamlit
google-generativeai
python-dotenv
