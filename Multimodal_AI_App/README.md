# 🤖 Multimodal AI Playground

**Explore the fusion of text, image, and video intelligence — all in one interactive web app.**  

This Streamlit-powered playground leverages Google Gemini's multimodal capabilities to showcase real-time AI applications, including image generation, image captioning, and YouTube video summarization.

---

## ✨ Features

### 📷 AI Image Generator
> _“Describe it, and watch it come to life.”_  
Turn text prompts into visually stunning AI-generated images using Google Gemini’s image generation model.

### 🖼️ AI Image Captioning
> _“What’s in this pic?”_  
Upload an image and let the AI describe it for you in natural language — ideal for accessibility and curiosity.

### 🎥 YouTube Video Summarizer
> _“No time to watch? Get a summary instead.”_  
Paste a YouTube video link and receive an AI-generated concise summary of the content.

---

## 🚀 Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io/)
- **AI Models**: [Google Gemini](https://deepmind.google/technologies/gemini/)
- **Environment Management**: `python-dotenv` for secure API key handling
- **Session State**: Personalized user experience and usage tracking with `st.session_state`

---

## 🧠 What I Learned

- ✅ Built a real-world app integrating multimodal AI with a user-friendly interface  
- ✅ Explored text-to-image and image-to-text conversion using Google Gemini  
- ✅ Implemented session state for tracking user interaction and personalization  
- ✅ Handled API key management securely via `.env` files  
- ✅ Focused on user experience with loading spinners, success messages, and error handling

---

## 💡 How to Run Locally

```bash
# Clone the repo
git clone 
cd Multimodal_AI_App

# Set up virtual environment (optional)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add your API key in .env
echo "GEMINI_API_KEY=your_gemini_api_key_here" > .env

# Run the app
streamlit run MultimodalApp.py
```

## 📌 Live Demo
🔗 Try it out: https://multimodal-ai-playground.streamlit.app

📂 Project Structure

.
├── MultimodalApp.py               # Main entry point

├── pages
    ├── 1_Image_Generator.py             # AI Image Generator tool
    ├── 2_Image_Caption_Generator.py   # AI Image Captioning tool
    ├── 3_Youtube_Video_Summarizer.py  # YouTube Video Summarizer
    
├── utils.py                       # Gemini client utility

├── .env                           # API key storage (not shared)

└── requirements.txt               # Required Python packages
