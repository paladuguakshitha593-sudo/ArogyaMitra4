from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_agent import ai_agent

router = APIRouter()

class MealPlanRequest(BaseModel):
    diet_type: str  # Veg, Non-Veg, Vegan
    calories: int

@router.post("/meal-plan")
async def get_meal_plan(request: MealPlanRequest):
    prompt = f"Create a 1-day {request.diet_type} meal plan totaling approximately {request.calories} calories."
    response = await ai_agent.generate_response(prompt)
    return {"meal_plan": response}