def match_candidate_to_job(resume_data: dict, job_description: str) -> dict:
    job_description = job_description.lower()
    job_keywords = job_description.split()

    score = 0
    for skill in resume_data["skills"]:
        if skill in job_keywords:
            score += 1

    match_percent = int((score / len(resume_data["skills"])) * 100) if resume_data["skills"] else 0

    return {
        "match_score": match_percent,
        "matched_skills": [s for s in resume_data["skills"] if s in job_keywords]
    }
