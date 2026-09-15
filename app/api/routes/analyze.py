from fastapi import APIRouter, UploadFile, File

from app.schemas.resume import ResumeOutput
from app.services.analyzer import analyze_resume
from app.services.parser import extract_text_from_pdf

router = APIRouter()


@router.post("/analyze-pdf", response_model=ResumeOutput)
async def analyze_pdf(file: UploadFile = File(...)) -> ResumeOutput:
    """Extract resume text from an uploaded PDF and analyze it."""
    text = extract_text_from_pdf(file.file)
    return analyze_resume(text)
