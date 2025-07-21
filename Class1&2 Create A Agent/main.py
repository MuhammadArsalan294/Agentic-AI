#CLASSWORK

#uv venv OR .venv\Scripts\active OR uv init .   run this command line 
#.env                                           create this file and generate api key
#uv add python-dotenv                           run this command line 
#uv add openai-agents                           run this command line 

from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Runner
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file / Python Dotenv Package /  uv add python-dotenv  
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
# print(gemini_api_key) # python main.py

# Check if the API key is present; if not, raise an error / Connection With Your LLM / Learn Agentic AI Code Copy Paste
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="models/gemini-1.5-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# / Openai Agents SDK / uv add openai-agents 
agent = Agent(
    name="Writer Agent",
    instructions="Your task is to answer user query. If you do not have the answer to the user query just deny. Do not hallucinate.",
)

response = Runner.run_sync(
    agent,
    input = 'What is the next.js app router? ',
    run_config = config 
)
print(response)
# OR print(response.final_output)


