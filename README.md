# 🧠 AI Foundations Projects

A collection of 10 AI-powered applications built using:

- Ollama (local LLM)
- Streamlit (UI)
- Python (service-based architecture)

---

## 🧱 Architecture

UI (Streamlit)
→ Service Layer
→ LLM Layer (Ollama)

---

## 🚀 Projects

- Resume Analyzer
- Blog Generator
- Chatbot
- Code Explainer
- Cover Letter Generator
- Email Reply Assistant
- FAQ Generator
- Grammar Tool
- PDF Parser
- Summarizer

---

## ⚙️ Setup

```bash
uv venv
source .venv/bin/activate
uv pip install streamlit ollama pypdf python-dotenv typer rich

# 📦 4. Create `requirements.txt`
```bash
uv pip freeze > requirements.txt

# pull olla
ollama pull llama3

#run the application
streamlit run ui/app.py