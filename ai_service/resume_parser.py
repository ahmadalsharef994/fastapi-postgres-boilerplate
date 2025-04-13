import re

def extract_skills(text: str) -> list:
    # Dummy keyword-based skill extraction
    skills_db = ["python", "fastapi", "docker", "postgresql", "aws", "pandas", "tensorflow"]
    text = text.lower()
    found = [skill for skill in skills_db if skill in text]
    return found

def extract_experience(text: str) -> int:
    # Dummy experience extractor (e.g., "3 years", "5+ years")
    matches = re.findall(r"(\d+)\s*\+?\s*years?", text.lower())
    return int(matches[0]) if matches else 0

def parse_resume(text: str) -> dict:
    return {
        "skills": extract_skills(text),
        "years_experience": extract_experience(text),
    }
