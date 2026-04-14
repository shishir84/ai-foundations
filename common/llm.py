import ollama

def generate_response(prompt: str, model="llama3"):
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content']