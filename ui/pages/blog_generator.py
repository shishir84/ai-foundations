import streamlit as st
from services.blog_generator_service import generate_blog
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

st.title("📝 Blog Generator")

topic = st.text_input("Enter topic")

if st.button("Generate"):
    result = generate_blog(topic)
    st.write(result)