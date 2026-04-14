import streamlit as st
from services.resume_analyzer_service import analyze_resume
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
st.title("📄 Resume Analyzer")

resume = st.text_area("Resume")
job = st.text_area("Job Description")

if st.button("Analyze"):
    if resume and job:
        with st.spinner("Analyzing..."):
            result = analyze_resume(resume, job)
            st.write(result)
    else:
        st.warning("Provide both inputs")