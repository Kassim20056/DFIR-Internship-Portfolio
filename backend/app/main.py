from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="AI DFIR Expert System", version="1.0.0")

# Setup CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure upload directories exist
os.makedirs("data/uploads", exist_ok=True)
os.makedirs("data/reports", exist_ok=True)

# Mount static files and routers
from app.routers import evidence, analysis, reports
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app.include_router(evidence.router)
app.include_router(analysis.router)
app.include_router(reports.router)

templates = Jinja2Templates(directory="../frontend/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")
