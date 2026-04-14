from common.llm import generate_response

def explain_code(code_snippet: str):
    prompt = f"""
    Explain the code and give the best practices.

    Code Snippet:
    {code_snippet}
    """
    return generate_response(prompt)
