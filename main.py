import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 1. Database Imports
from app.database import engine, Base

# 2. Model Imports (Required for SQLAlchemy to see the tables)
from app.models.user import User 
from app.models.health import HealthAssessment

# 3. Router Imports (The 'Doors' to your API)
# Check: Are these files named EXACTLY like this in your routers folder?
from app.routers import chat
from app.routers import workouts
from app.routers import nutrition

# Initialize Database Tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ArogyaMitra API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registering Routers
app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])
app.include_router(workouts.router, prefix="/api/workouts", tags=["Workouts"])
app.include_router(nutrition.router, prefix="/api/nutrition", tags=["Nutrition"])

@app.get("/")
async def root():
    return {"message": "ArogyaMitra is Online"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)