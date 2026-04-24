# Resume Analyzer API 

A FastAPI-based backend system that analyzes resumes and provides structured feedback.

## Features

*  Resume scoring (skills, experience, projects)
*  Smart feedback generation
*  PDF resume upload support
*  FastAPI backend with clean architecture

## Tech Stack

* FastAPI
* Python
* PyPDF2
* Uvicorn

## Project Structure

```
app/
 ├── api/
 ├── services/
 ├── schemas/
 ├── main.py
data/
requirements.txt
```

## Run Locally

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

## API Endpoints

* `/analyze` → Analyze resume text
* `/analyze-pdf` → Upload and analyze PDF

## Future Improvements

* NLP-based skill extraction
* LLM-powered feedback
* Frontend dashboard
