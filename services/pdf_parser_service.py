from common.llm import generate_response

def pdf_parser(pdf_text: str):
    prompt = f"""
    Extract the key information and summarize the following PDF content:

    PDF Content:
    {pdf_text}
    """
    return generate_response(prompt)

