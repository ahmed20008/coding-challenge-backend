from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas.application import ApplicationResponse
from models.application import Application

router = APIRouter()

@router.get("/", response_model=List[ApplicationResponse])
def list_applications(db: Session = Depends(get_db)):
    """
    Get overview of all applications in the database.
    """
    applications = db.query(Application).all()
    return applications