import os
from dotenv import load_dotenv
from google import genai

# Load environment variables once
load_dotenv()

def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set in the .env file.")
    return genai.Client(api_key=api_key)
