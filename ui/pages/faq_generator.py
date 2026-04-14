import streamlit as st
from services.chatbot_service import chat
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

st.title(" FAQ Generator ")

topic = st.text_input("Enter topic")
if st.button("Generate FAQs"):
    if topic:
        with st.spinner("Generating..."):
            result = chat(f"Generate a list of frequently asked questions (FAQs) and their answers on the topic of:\n\n{topic}\n\nInclude at least 5 questions and answers.")
            st.write(result)
    else:
        st.warning("Provide a topic")
        