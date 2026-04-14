import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

st.set_page_config(page_title="AI Foundations", layout="wide")

st.title("🧠 AI Projects Dashboard")

projects = [
    ("Resume Analyzer", "resume_analyzer"),
    ("Blog Generator", "blog_generator"),
    ("Chatbot", "chatbot"),
    ("Code Explainer", "code_explainer"),
    ("Cover Letter", "cover_letter"),
    ("Email Reply", "email_reply"),
    ("FAQ Generator", "faq_generator"),
    ("Grammar Tool", "grammar_tool"),
    ("PDF Parser", "pdf_parser"),
    ("Summarizer", "summarizer"),
]

cols = st.columns(3)

for i, (name, page) in enumerate(projects):
    if cols[i % 3].button(name):
        st.switch_page(f"pages/{page}.py")