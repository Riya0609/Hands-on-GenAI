import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv
from utils import get_gemini_client

tool_name = "image_generator"  # Change this per page

if tool_name not in st.session_state:
    st.session_state[tool_name] = 0

st.set_page_config(page_title="Image Generator", page_icon="📷")

client = get_gemini_client()

st.title("AI Image Generator")

user_prompt = st.text_input("What do you want to generate image for?")

if st.button("Generate Image"):
    if not user_prompt:
        st.warning("Please enter the prompt!!")
    else:
        try:
            st.session_state[tool_name] += 1 # Increment on action (e.g. button click)
            with st.spinner("Generating image..."):
                response = client.models.generate_content(
                    model="gemini-2.0-flash-exp-image-generation",
                    contents=user_prompt,
                    config=types.GenerateContentConfig(
                        response_modalities=['Text', 'Image']
                    )
                )

            st.subheader("Generated Image")

            for part in response.candidates[0].content.parts:
                if part.text is not None:
                    st.write(part.text)
                elif part.inline_data is not None:
                    image = Image.open(BytesIO((part.inline_data.data)))
                    st.image(image)

        except Exception as e:
            st.error(f"Error generating image: {e}")

