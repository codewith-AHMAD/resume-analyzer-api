from fastapi import APIRouter, UploadFile, File
from app.schemas.resume import ResumeInput, ResumeOutput
from app.services.analyzer import analyze_resume
from app.services.parser import extract_text_from_pdf

router = APIRouter()

# @router.post("/analyze", response_model=ResumeOutput)
# def analyze(data: ResumeInput):
#     return analyze_resume(data.text)

@router.post("/analyze-pdf", response_model=ResumeOutput)
async def analyze_pdf(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file.file)
    return analyze_resume(text)