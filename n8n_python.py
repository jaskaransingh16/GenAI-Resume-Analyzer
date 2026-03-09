import streamlit as st
import google.generativeai as genai
import requests
from PyPDF2 import PdfReader
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")
def extract_text(file):
    if file.type == "application/pdf":
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    elif file.type == "text/plain":
        return file.read().decode("utf-8")
    else:
        st.error("Unsupported file type. Please upload PDF or TXT.")
        return None

## Extract Skills with Gemini
def extract_skills_with_gemini(text):
    prompt = f"""
    Extract the 8-10 most relevant professional skills from the following resume text.
    Return them as a clean comma-separated list (no explanation).

    Resume:
    {text[:6000]}  # truncate to avoid token overflow
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    skills_text = response.text.strip()
    skills = [s.strip() for s in skills_text.replace("\n", ",").split(",") if s.strip()]
    return skills[:10]

## Extract Summary with N8N  
def get_summary_from_n8n(text):
    payload = {"resume_text": text}
    try:
        response = requests.post(N8N_WEBHOOK_URL, json=payload, timeout=30)
        if response.status_code == 200:
            return response.json().get("summary", "No summary returned.")
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Request failed: {str(e)}"
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.title("📄 AI-Powered Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])

if uploaded_file:
    with st.spinner("Extracting text..."):
        text = extract_text(uploaded_file)

    if text:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🧠 Extracting Skills...")
            skills = extract_skills_with_gemini(text)
            st.success("Top Skills Identified")
            st.write(", ".join(skills))

        with col2:
            st.subheader("✍️ Generating Professional Summary...")
            summary = get_summary_from_n8n(text)
            st.success("Summary Generated")
            st.write(summary)


