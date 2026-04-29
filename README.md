# AI API Gateway

A Python REST API that connects to multiple AI models through a single unified endpoint. You send a question and specify which AI you want to use, and the API routes your request to the right provider and returns the response.

## Live API

Test it directly in your browser — no setup needed:

👉 [https://ai-api-ga55.onrender.com/docs](https://ai-api-ga55.onrender.com/docs)

> Note: The free server sleeps when inactive. If it takes a few seconds to respond, just wait and try again.

## Supported AI Models

- **ChatGPT** via OpenAI
- **Claude** via Anthropic
- **LLaMA 3.3** via Groq

## How to use the API

Send a POST request to `/ask` with a prompt and a model name:

```json
{
  "prompt": "What is the capital of Morocco?",
  "model": "groq"
}
```

Model options: `chatgpt`, `claude`, `groq`

## How to run locally

1. Clone the repository
2. Install dependencies: