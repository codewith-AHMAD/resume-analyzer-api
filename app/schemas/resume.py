from pydantic import BaseModel
from typing import List, Dict

class ResumeInput(BaseModel):
    text: str



class ResumeOutput(BaseModel):
    score: int
    skills_found: List[str]
    missing_skills: List[str]
    suggestions: List[str]
    breakdown: Dict[str, int]