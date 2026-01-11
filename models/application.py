from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()

class EmploymentMode(str, enum.Enum):
    FREELANCE = "freelance"
    EMPLOYED = "employed"

class Capacity(str, enum.Enum):
    PART_TIME = "part-time"
    FULL_TIME = "full-time"

class Application(Base):
    __tablename__ = "applications"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    github_user = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    projects = relationship("Project", back_populates="application", cascade="all, delete-orphan")

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("applications.id", ondelete="CASCADE"))
    name = Column(String, nullable=False)
    employment_mode = Column(Enum(EmploymentMode), nullable=False)
    capacity = Column(Enum(Capacity), nullable=False)
    duration_months = Column(Float, nullable=False)
    start_year = Column(Integer, nullable=False)
    role = Column(String, nullable=False)
    team_size = Column(Integer, nullable=False)
    repository_link = Column(String, nullable=True)
    live_url = Column(String, nullable=True)
    
    application = relationship("Application", back_populates="projects")
