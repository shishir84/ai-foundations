from common.llm import generate_response

def generate_email_reply(email_text: str):
    prompt = f"""
    Generate a professional email reply to the following email:

    Email:
    {email_text}
    """
    return generate_response(prompt)    
