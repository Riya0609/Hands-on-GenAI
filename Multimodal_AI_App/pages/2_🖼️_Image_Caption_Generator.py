import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv
from utils import get_gemini_client

tool_name = "image_caption_generator"  

if tool_name not in st.session_state:
    st.session_state[tool_name] = 0


st.set_page_config(page_title="Image Caption Generator", page_icon="🖼️")

client = get_gemini_client()

st.title("AI Image Caption Generator")

uploaded_image = st.file_uploader("Upload an image for caption generation", type=["jpg", "jpeg", "png"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded image")

    if st.button("Generate caption"):
        try:
            st.session_state[tool_name] += 1
            with st.spinner("Generating caption..."):
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=[image, "What is this image?"]
                )
                st.subheader("Generated caption:")
                st.write(response.text)

        except Exception as e:
            st.error(f"Error generating caption: {e}")
