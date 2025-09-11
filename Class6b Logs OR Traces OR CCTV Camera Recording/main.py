#uv venv OR .venv\Scripts\active OR uv init .   run this all command line 
#.env                                           create this file and generate api key
#uv add python-dotenv                           run this command line 
#uv add openai-agents                           run this command line 


from dotenv import load_dotenv
import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# Load the environment variables from the .env file / Python Dotenv Package /  uv add python-dotenv  
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error / Connection With Your LLM / Learn Agentic AI Code Copy Paste
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
   #tracing_disabled=True   # Es ka mtlb hai tracing naw karo / ka matlab hai ke tracing feature ko disable kar diya gaya hai. OR agar tracing karni hai tw es ko remove karna lazmi hoga ya false krna hoga
   #tracing_disabled=False # Es ka mtlb hai tracing karo / ka matlab hai ke tracing enabled hai
)