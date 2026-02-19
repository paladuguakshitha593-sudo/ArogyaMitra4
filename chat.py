from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_agent import ai_agent

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/aromi-chat")
async def chat_with_aromi(request: ChatRequest):
    response = await ai_agent.generate_response(request.message)
    return {"response": response}