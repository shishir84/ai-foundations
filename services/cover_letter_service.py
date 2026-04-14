from common.llm import generate_response

def generate_cover_letter(resume_text: str, job_desc: str):
    prompt = f"""
    Generate a cover letter based on the resume and job description.

    Resume:
    {resume_text}

    Job:
    {job_desc}
    """
    return generate_response(prompt)
        