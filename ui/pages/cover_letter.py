import streamlit as st
from services.chatbot_service import chat
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

st.title(" Cover Letter Generator")
job_description = st.text_area("Enter job description")
if st.button("Generate Cover Letter"):
    if job_description:
        with st.spinner("Generating..."):
            result = chat(f"Generate a cover letter for the following job description:\n\n{job_description}")
            st.write(result)
    else:
        st.warning("Provide a job description")