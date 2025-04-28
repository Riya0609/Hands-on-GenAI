import os
from dotenv import load_dotenv
from google import genai
import streamlit as st

# Load environment variables once
load_dotenv()

def get_gemini_client():
    api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set. Please check your Streamlit secrets or .env file.")
    return genai.Client(api_key=api_key)
