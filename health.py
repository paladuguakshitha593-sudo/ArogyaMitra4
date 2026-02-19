from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.database import Base

class HealthAssessment(Base):
    __tablename__ = "health_assessments"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    weight = Column(Float)
    height = Column(Float)
    age = Column(Integer)
    gender = Column(String)
    goal = Column(String)  # e.g., "Weight Loss", "Muscle Gain"