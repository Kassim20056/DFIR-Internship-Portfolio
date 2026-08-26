from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class UploadResponse(BaseModel):
    filename: str
    message: str
    file_id: str

class AnalysisRequest(BaseModel):
    file_id: str

class ThreatIntel(BaseModel):
    indicator: str
    type: str
    description: str

class AnalysisResult(BaseModel):
    status: str
    summary: str
    iocs: List[ThreatIntel]
    mitre_attack: List[str]
    timeline: List[Dict[str, Any]]
    confidence_score: float
