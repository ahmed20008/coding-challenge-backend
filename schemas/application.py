from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from enum import Enum
from datetime import datetime

class EmploymentModeEnum(str, Enum):
    FREELANCE = "freelance"
    EMPLOYED = "employed"

class CapacityEnum(str, Enum):
    PART_TIME = "part-time"
    FULL_TIME = "full-time"

class ProjectBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    employment_mode: EmploymentModeEnum
    capacity: CapacityEnum
    duration_months: float = Field(..., gt=0, description="Duration in months")
    start_year: int = Field(..., ge=1970, le=2100)
    role: str = Field(..., min_length=1, max_length=200)
    team_size: int = Field(..., gt=0)
    repository_link: Optional[str] = None
    live_url: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: int
    
    class Config:
        from_attributes = True

class ApplicationBase(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=1, max_length=200)
    github_user: str = Field(..., min_length=1, max_length=100)

class ApplicationCreate(ApplicationBase):
    projects: List[ProjectCreate] = Field(..., min_length=1)

class ApplicationResponse(ApplicationBase):
    id: int
    projects: List[ProjectResponse]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
