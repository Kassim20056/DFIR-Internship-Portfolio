from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os
from app.routers.analysis import ANALYSIS_RESULTS
from app.services.reporter import ReportGenerator

router = APIRouter(prefix="/api/v1/reports", tags=["reports"])

@router.get("/generate/{file_id}")
def generate_report(file_id: str):
    if file_id not in ANALYSIS_RESULTS:
        raise HTTPException(status_code=404, detail="Analysis result not found")

    result_data = ANALYSIS_RESULTS[file_id]

    if result_data.get("status") != "Complete":
        raise HTTPException(status_code=400, detail="Analysis is not yet complete")

    try:
        generator = ReportGenerator(result=result_data["data"])
        pdf_path = generator.generate_pdf()

        return FileResponse(
            path=pdf_path,
            filename=f"DFIR_Report_{file_id}.pdf",
            media_type="application/pdf"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate report: {str(e)}")
