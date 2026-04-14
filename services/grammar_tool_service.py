from common.llm import generate_response

def grammar_tool(text: str):
    prompt = f"""
    Check the grammar of the following text and provide corrections if needed:

    Text:
    {text}
    """
    return generate_response(prompt)    

