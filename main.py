import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import anthropic
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# I added this because without it the browser was blocking requests from the HTML page
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# My API Keys:
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# What the user sends to my API
class PromptRequest(BaseModel):
    prompt: str
    model: str

# My main endpoint
@app.post("/ask")
def ask_ai(request: PromptRequest):

    # this checks which AI the user wants and sends the request to the right one
    if request.model == "chatgpt":
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request.prompt}]
        )
        return {"model": "chatgpt", "response": response.choices[0].message.content}

    elif request.model == "claude":
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            messages=[{"role": "user", "content": request.prompt}]
        )
        return {"model": "claude", "response": response.choices[0].text}

    elif request.model == "groq":
        client = Groq(api_key=GROQ_API_KEY)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": request.prompt}]
        )
        return {"model": "groq", "response": response.choices[0].message.content}

    else:
        return {"error": "Invalid model. Choose 'chatgpt', 'claude' or 'groq'"}

