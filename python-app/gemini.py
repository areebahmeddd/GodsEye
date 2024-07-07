# Core library imports: Google Generative AI setup
import streamlit as st
import google.generativeai as genai
from google.generativeai import GenerativeModel
from typing import Dict, Any

# Local project-specific imports: Gemini API key from .env
from config import GEMINI_API_KEY

# Load Gemini API key from Streamlit secrets.toml
# GEMINI_API_KEY = st.secrets["gemini"]["api_key"]
genai.configure(api_key=GEMINI_API_KEY)

# Generation settings to control the model's output
generation_config = {
    'temperature': 1,
    'top_p': 0.95,
    'top_k': 64,
    'max_output_tokens': 8192,
    'response_mime_type': 'text/plain'
}

# Safety settings to block harmful content (BLOCK_NONE is set to ignore triggers in scraped articles for accurate context processing)
# Thresholds: BLOCK_NONE, BLOCK_LOW_AND_ABOVE, BLOCK_MEDIUM_AND_ABOVE, BLOCK_ONLY_HIGH
safety_settings = [
    {'category': 'HARM_CATEGORY_HARASSMENT', 'threshold': 'BLOCK_NONE'},
    {'category': 'HARM_CATEGORY_HATE_SPEECH', 'threshold': 'BLOCK_NONE'},
    {'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT', 'threshold': 'BLOCK_NONE'},
    {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT', 'threshold': 'BLOCK_NONE'}
]

# Load system instructions for the Gemini model
with open('gemini_instructions.md', 'r') as file:
    gemini_instructions = file.read()

# Initialize the Gemini model with custom settings and instructions
llm = GenerativeModel(
    model_name='gemini-1.5-flash-latest',
    generation_config=generation_config,
    safety_settings=safety_settings,
    system_instruction=gemini_instructions
)

# Start a chat session with the Gemini model
chat_session = llm.start_chat(history=[])

def perspec(news_data: Dict[str, Any]) -> Dict[str, Any]:
    # Send the news data to the Gemini model as plain text due to formatting requirements
    user_message = f'News Data: {news_data}'
    bot_response = chat_session.send_message(user_message)

    # Filter out the JSON code block and return the response as a dictionary
    filtered_response = bot_response.text.replace('```json', '').replace('```', '')
    return eval(filtered_response) # If eval() throws an error, use ast.literal_eval() or json.loads() instead
