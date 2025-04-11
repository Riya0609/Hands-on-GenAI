import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv
from utils import get_gemini_client

tool_name = "youtube_video_summarizer"  

if tool_name not in st.session_state:
    st.session_state[tool_name] = 0


st.set_page_config(page_title="YouTube Video Summarizer", page_icon="🎥")

client = get_gemini_client()

st.title("AI Youtube Video Summarizer")

youtube_url = st.text_input("Enter YouTube Video URL")

if st.button("Video Summarizer"):
    if not youtube_url:
        st.warning("No YouTube Url present!!")
    else:
        try:
            st.session_state[tool_name] += 1
            with st.spinner("Generating video summary..."):
                response = client.models.generate_content(
                    model='models/gemini-2.0-flash',
                    contents=types.Content(
                        parts=[
                            types.Part(text='Can you summarize this video?'),
                            types.Part(
                                file_data=types.FileData(file_uri=youtube_url)
                            )
                        ]
                    )
                )
            st.subheader("Video Summary")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error generating summary")
            