from common.llm import generate_response

def analyze_resume(resume_text: str, job_desc: str):
    prompt = f"""
    Analyze the resume against job description.

    Resume:
    {resume_text}

    Job:
    {job_desc}

    Provide:
    - Match score
    - Missing skills
    - Suggestions
    """
    return generate_response(prompt)