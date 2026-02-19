from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base  # Keep this

class HealthAssessment(Base):
    __tablename__ = "health_assessments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    age = Column(Integer)
    gender = Column(String)
    height = Column(Float)
    weight = Column(Float)
    bmi = Column(Float, nullable=True)
    
    medical_history = Column(String, default="None")
    health_conditions = Column(String, default="None")
    injuries = Column(String, default="None")
    allergies = Column(String, default="None")
    medications = Column(String, default="None")
    
    fitness_level = Column(String, default="beginner")
    fitness_goal = Column(String)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())