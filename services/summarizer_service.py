from common.llm import generate_response

def summarize_text(text: str):
    prompt = f"""
    Summarize the following text in a concise manner:

    Text:
    {text}
    """
    return generate_response(prompt)

