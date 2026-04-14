import streamlit as st
from services.chatbot_service import chat
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

st.title(" Grammar Tool")

text = st.text_area("Enter text to check grammar")
if st.button("Check Grammar"):
    if text:
        with st.spinner("Checking grammar..."):
            result = chat(f"Check the grammar of the following text and provide corrections if needed:\n\n{text}")
            st.write(result)
    else:
        st.warning("Provide some text to check grammar")