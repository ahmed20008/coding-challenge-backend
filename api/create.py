from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.application import ApplicationCreate, ApplicationResponse
from models.application import Application, Project

router = APIRouter()

@router.post("/", response_model=ApplicationResponse, status_code=status.HTTP_201_CREATED)
def create_application(application: ApplicationCreate, db: Session = Depends(get_db)):
    """
    Submit a new application. If email exists, old data is automatically deleted.
    """
    existing_app = db.query(Application).filter(Application.email == application.email).first()
    if existing_app:
        db.delete(existing_app)
        db.commit()
    
    db_application = Application(
        email=application.email,
        name=application.name,
        github_user=application.github_user
    )
    db.add(db_application)
    db.flush()
    
    for project_data in application.projects:
        db_project = Project(**project_data.model_dump(), application_id=db_application.id)
        db.add(db_project)
    
    db.commit()
    db.refresh(db_application)
    return db_application