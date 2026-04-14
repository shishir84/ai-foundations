import streamlit as st
from services.chatbot_service import chat
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

st.title(" Email Reply Generator ")
email_text = st.text_area("Enter email text")
if st.button("Generate Reply"):
    if email_text:
        with st.spinner("Generating..."):
            result = chat(f"Generate a professional email reply to the following email:\n\n{email_text}")
            st.write(result)
    else:
        st.warning("Provide an email text")