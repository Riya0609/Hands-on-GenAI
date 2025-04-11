import streamlit as st

st.set_page_config(
    page_title="Multimodal AI Playground",
    page_icon="🤖",
    layout="centered",
)

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if st.session_state.user_name == "":
    name_input = st.text_input("👋 Welcome! What's your name?")
    if name_input:
        st.session_state.user_name = name_input
        st.success(f"Nice to meet you, {name_input}!")
        st.rerun()
else:
    st.markdown(f"### 👋 Welcome back, **{st.session_state.user_name}**!")

#st.markdown("#### 📊 Your session stats:")

#st.write(f"- 📷 Image Generator used: {st.session_state.get('image_generator', 0)} times")
#st.write(f"- 🖼️ Image Captioning used: {st.session_state.get('image_caption_generator', 0)} times")
#st.write(f"- 🎥 Video Summarizer used: {st.session_state.get('youtube_video_summarizer', 0)} times")

#if st.button("🔄 Reset session"):
#    st.session_state.clear()
#    st.rerun()


st.markdown("<h1 style='text-align: center;'>🤖 Multimodal AI Playground</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>One App. Three Superpowers. Unlimited Creativity. 🚀</h3>", unsafe_allow_html=True)

st.markdown("---")

# HERO SECTION
st.markdown("### ✨ What’s inside?")
st.markdown(
    """
    #### 📷 **AI Image Generator**
    > _Describe it, and watch it come to life._  
    Turn your ideas into visuals using cutting-edge image generation from Gemini AI.

    #### 🖼️ **Image Caption Generator**
    > _What’s in this pic?_  
    Let the AI analyze any image and describe it intelligently — perfect for accessibility and curiosity.

    #### 🎥 **YouTube Video Summarizer**
    > _No time to watch? No problem._  
    Paste a YouTube link and get a smart summary of the content in seconds.
    """
)

st.markdown("---")

# FEATURES
st.markdown("### 💡 Why you’ll love this app")
st.markdown(
    """
    - ⚡ **Fast & Interactive** – Built with [Streamlit](https://streamlit.io) for a seamless user experience.
    - 🧠 **Powered by Google Gemini AI** – One of the smartest models around, now in your hands.
    - 🔐 **Secure** – Your API keys are safe thanks to `.env` integration.
    - 🎯 **Purpose-Driven Design** – Each tool is focused, simple, and effective.

    ---
    """
)

with st.expander("📊 Your session stats", expanded=False):
    st.write(f"- 📷 Image Generator used: {st.session_state.get('image_generator', 0)} times")
    st.write(f"- 🖼️ Image Captioning used: {st.session_state.get('image_caption_generator', 0)} times")
    st.write(f"- 🎥 Video Summarizer used: {st.session_state.get('youtube_video_summarizer', 0)} times")
    if st.button("🔄 Reset session"):
        st.session_state.clear()
        st.rerun()

# CTA
st.markdown("<h3 style='text-align: center;'>Ready to explore the future of AI?</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>👉 Select a tool from the sidebar and dive in!</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Create. Caption. Summarize. ✨</p>", unsafe_allow_html=True)
