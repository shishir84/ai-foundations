from common.llm import generate_response

def generate_blog(topic: str):
    prompt = f"""
    Write an SEO optimized blog on:
    {topic}

    Include headings, keywords, and conclusion.
    """
    return generate_response(prompt)