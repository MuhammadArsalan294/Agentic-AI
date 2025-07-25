# uv venv OR .venv\Scripts\activate OR uv init . / Run this All Command
# .env file                                      / Create A File Name            
# uv add python-dotenv                           / Run this Command
# uv add openai-agents                           / Run this Command

from dotenv  import load_dotenv
import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# Python Dotenv Package
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Connection With Your LLM / Panaversity Copy Paste
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


