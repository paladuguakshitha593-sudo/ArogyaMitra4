import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class ArogyaMitraAgent:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=api_key) if api_key else None

    async def generate_response(self, message: str):
        if not self.client: return "AI Error: No API Key."
        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": "You are AROMI, a health coach."},
                      {"role": "user", "content": message}]
        )
        return completion.choices[0].message.content

ai_agent = ArogyaMitraAgent()