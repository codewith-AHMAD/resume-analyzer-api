from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SKILLS_PATH = BASE_DIR / "data" / "skills.txt"


def load_skills():
    with open(SKILLS_PATH) as f:
        return [line.strip().lower() for line in f]

import re

def analyze_resume(text: str):
    text_lower = text.lower()
    skills = load_skills()

    words = set(re.findall(r'\b\w+\b', text_lower))

    found = []
    for skill in skills:
        skill_tokens = skill.split()
        if all(token in words for token in skill_tokens):
            found.append(skill)

    missing = [s for s in skills if s not in found]

    score = int((len(found) / len(skills)) * 100)

    suggestions = []
    if score < 50:
        suggestions.append("Add more relevant technical skills.")
    if "project" not in text_lower:
        suggestions.append("Include project experience.")
    if "experience" not in text_lower:
        suggestions.append("Mention work experience.")
    if len(missing) > 0:
        suggestions.append(f"Consider adding skills like: {', '.join(missing[:3])}")

    skills_score = int((len(found) / len(skills)) * 60)

    experience_score = 20 if "experience" in text_lower else 0
    projects_score = 20 if "project" in text_lower else 0

    total_score = skills_score + experience_score + projects_score

    breakdown = {
        "skills": skills_score,
        "experience": experience_score,
        "projects": projects_score
    }

    return {
        "score": total_score,
        "skills_found": found,
        "missing_skills": missing[:5],
        "suggestions": suggestions,
        "breakdown": breakdown
    }