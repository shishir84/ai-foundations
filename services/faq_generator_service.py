from common.llm import generate_response

def faq_generator(topic: str):
    prompt = f"""
    Generate a list of frequently asked questions (FAQs) and their answers on the topic of:
    {topic}

    Include at least 5 questions and answers.
    """
    return generate_response(prompt)

