import streamlit as st
from services.chatbot_service import chat
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

st.title("💬 Chatbot")

user_input = st.text_input("Ask something")

if st.button("Send"):
    response = chat(user_input)
    st.write(response)