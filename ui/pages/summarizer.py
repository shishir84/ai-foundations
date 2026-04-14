import streamlit as st
from services.resume_analyzer_service import analyze_resume
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
st.title(" Summarizer ")

text = st.text_area("Enter text to summarize")
if st.button("Summarize"):  
    if text:
        with st.spinner("Summarizing..."):
            result = analyze_resume(text, "")
            st.write(result)
    else:
        st.warning("Provide some text to summarize")