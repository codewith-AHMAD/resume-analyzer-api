from fastapi import FastAPI
from app.api.routes.analyze import router as analyze_router

app = FastAPI(title="Resume Analyzer API")

app.include_router(analyze_router)