import streamlit as st
from services.chatbot_service import chat
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

st.title(" PDF Parser")

#upload the file for parsing
pdf_file = st.file_uploader("Upload PDF", type="pdf")
if pdf_file is not None:
    # Process the uploaded PDF file
    passed_pdf_text = pdf_file.read().decode("utf-8", errors="ignore")
    with st.spinner("Parsing PDF..."):
        result = chat(f"Extract the key information and summarize the following PDF content:\n\n{passed_pdf_text}")
        st.write(result)

