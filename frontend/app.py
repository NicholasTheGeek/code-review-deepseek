import streamlit as st
import requests
from streamlit_lottie import st_lottie
import json

#Page Configuration
st.set_page_config(
    page_title="AI Code Review Assistant",
    page_icon="🧠",
    layout="wide",
)

#Custom CSS
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
            font-family: 'Segoe UI', sans-serif;
        }
        .stTextArea textarea {
            font-family: 'Courier New', monospace;
            font-size: 14px;
            border-radius: 10px;
        }
        .review-box {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .header-title {
            font-size: 48px;
            color: #002b36;
            font-weight: bold;
        }
        .sub-header {
            font-size: 20px;
            color: #586e75;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

#Header
st.markdown("""
    <div style='text-align: center'>
        <div class='header-title'>AI Code Review Assistant</div>
        <div class='sub-header'>Powered by DeepSeek + FastAPI</div>
    </div>
""", unsafe_allow_html=True)

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_ai = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_qp1q7mct.json")
st_lottie(lottie_ai, height=180, key="ai_lottie")

#Input Area
st.markdown("### 🔧 Paste your code below:")
code_input = st.text_area("", height=300, placeholder="e.g. def hello(): print('Hello, world')")

#Get Review
if st.button("🚀 Review My Code"):
    if code_input.strip():
        with st.spinner("Analyzing code with DeepSeek..."):
            try:
                response = requests.post("http://localhost:8000/review/", data={"code": code_input})
                review = response.json().get("review", "No feedback returned.")
                st.markdown("### 📋 Review & Suggestions")
                st.markdown(f"<div class='review-box'><pre>{review}</pre></div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please paste some code to review.")

#Footer
st.markdown("---")
st.markdown("Created with ❤️ by [Nicholas](https://www.linkedin.com/in/nicholas-masuku-74655582/) using [Streamlit](https://streamlit.io/) + [FastAPI](https://fastapi.tiangolo.com/) + [DeepSeek](https://ollama.ai/library/deepseek-coder)", unsafe_allow_html=True)

