from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from database import get_db
from models.application import Application
from services.pdf_generator import generate_pdf
import os

router = APIRouter()

@router.get("/{application_id}/pdf")
def download_pdf(application_id: int, db: Session = Depends(get_db)):
    """
    Generate and download PDF document for an application.
    """
    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    
    pdf_path = generate_pdf(application)
    
    if not os.path.exists(pdf_path):
        raise HTTPException(status_code=500, detail="Failed to generate PDF")
    
    return FileResponse(
        path=pdf_path,
        filename=f"{application.name}_application.pdf",
        media_type="application/pdf"
    )