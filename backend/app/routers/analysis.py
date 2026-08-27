from fastapi import APIRouter, HTTPException, BackgroundTasks
import os
from app.models.schemas import AnalysisRequest, AnalysisResult
from app.services.parser import ForensicParser
from app.services.ai_engine import AI_DFIR_Expert

router = APIRouter(prefix="/api/v1/analysis", tags=["analysis"])

UPLOAD_DIR = "data/uploads"

# In-memory store for analysis results for simulation purposes
# In production, this would be a database (PostgreSQL, MongoDB, etc.)
ANALYSIS_RESULTS = {}

@router.post("/start", response_model=dict)
async def start_analysis(request: AnalysisRequest, background_tasks: BackgroundTasks):
    """Starts the AI analysis process in the background."""
    # Find the file
    target_file = None
    for filename in os.listdir(UPLOAD_DIR):
        if filename.startswith(request.file_id):
            target_file = filename
            break

    if not target_file:
        raise HTTPException(status_code=404, detail="Evidence file not found")

    file_path = os.path.join(UPLOAD_DIR, target_file)

    # Initialize status
    ANALYSIS_RESULTS[request.file_id] = {"status": "Processing"}

    # Run analysis in background
    background_tasks.add_task(run_analysis_pipeline, request.file_id, file_path, target_file)

    return {"message": "Analysis started", "file_id": request.file_id, "status": "Processing"}

@router.get("/result/{file_id}", response_model=AnalysisResult)
async def get_analysis_result(file_id: str):
    """Retrieves the result of the AI analysis."""
    if file_id not in ANALYSIS_RESULTS:
        raise HTTPException(status_code=404, detail="Analysis result not found or not started")

    result = ANALYSIS_RESULTS[file_id]
    if result.get("status") == "Processing":
        # Return a partial/processing state
        return AnalysisResult(
            status="Processing",
            summary="The AI is currently analyzing the evidence...",
            iocs=[],
            mitre_attack=[],
            timeline=[],
            confidence_score=0.0
        )
    elif result.get("status") == "Error":
        raise HTTPException(status_code=500, detail=result.get("error_message", "Unknown error during analysis"))

    return result["data"]

def run_analysis_pipeline(file_id: str, file_path: str, filename: str):
    """Background task that runs parsing and AI analysis."""
    try:
        # 1. Parse the evidence
        parser = ForensicParser(file_path=file_path, filename=filename)
        parsed_data = parser.parse()

        # 2. Run AI Analysis
        ai_system = AI_DFIR_Expert()
        result: AnalysisResult = ai_system.analyze(parsed_data=parsed_data)

        # 3. Store Result
        ANALYSIS_RESULTS[file_id] = {
            "status": "Complete",
            "data": result
        }
    except Exception as e:
        ANALYSIS_RESULTS[file_id] = {
            "status": "Error",
            "error_message": str(e)
        }
