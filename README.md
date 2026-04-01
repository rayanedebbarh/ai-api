# My API

A Python API built with FastAPI that routes prompts to different AI models based on a model directive.

## Supported Models
- ChatGPT (OpenAI)
- Claude (Anthropic)
- Groq (LLaMA 3.3)

## How to run

1. Install dependencies:
   pip3 install fastapi uvicorn openai anthropic groq python-dotenv

2. Create a .env file with your API keys:
   OPENAI_API_KEY=your-key
   ANTHROPIC_API_KEY=your-key
   GROQ_API_KEY=your-key

3. Start the server:
   uvicorn main:app --reload

4. Open the interface:
   Open index.html in your browser

5. Or you can also test via Swagger UI:
   http://127.0.0.1:8000/docs