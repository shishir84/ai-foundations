import streamlit as st
from services.chatbot_service import chat
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

st.title(" Code Explainer")

code_snippet = st.text_area("Enter code snippet")
if st.button("Explain"):
    if code_snippet:
        with st.spinner("Explaining..."):
            result = chat(f"Explain the following code and give best practices:\n\n{code_snippet}")
            st.write(result)
    else:
        st.warning("Provide a code snippet")
        