# 🧠 GenAI Resume Analyzer

An AI-powered Resume Analyzer that evaluates resumes against job descriptions using **LLMs (GPT API)**.  
The application provides **skill gap analysis, improvement suggestions, and candidate suitability insights** through an interactive web interface.

The system also integrates **n8n automation workflows** to streamline resume processing and LLM-based analysis.

---

## 🚀 Features

- 📄 Upload and analyze resumes
- 🤖 AI-powered resume evaluation using GPT API
- 🧠 Skill gap analysis between resume and job description
- 📊 Structured improvement suggestions
- ⚡ Real-time feedback through a Streamlit interface
- 🔄 Automated workflow integration using n8n
- 🔍 NLP preprocessing to extract and compare candidate skills

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** – Interactive UI
- **OpenAI GPT API** – LLM-based analysis
- **n8n** – Workflow automation
- **NLP preprocessing** – Skill extraction and comparison

---

## 🧩 System Architecture

1. User uploads a resume and provides a job description.
2. NLP preprocessing extracts relevant candidate skills.
3. Resume and job description are sent to the **GPT API**.
4. The LLM generates:
   - Skill match analysis
   - Missing skills
   - Improvement suggestions
5. **n8n workflow** automates resume processing and response generation.
6. Results are displayed through the **Streamlit UI**.

---
