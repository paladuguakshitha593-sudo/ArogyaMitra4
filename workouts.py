from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_agent import ai_agent

router = APIRouter()

class WorkoutRequest(BaseModel):
    fitness_level: str  # Beginner, Intermediate, Advanced
    equipment: str      # None, Gym, Dumbbells

@router.post("/generate")
async def get_workout(request: WorkoutRequest):
    prompt = f"Generate a 30-minute {request.fitness_level} workout plan using {request.equipment} equipment."
    response = await ai_agent.generate_response(prompt)
    return {"workout_plan": response}