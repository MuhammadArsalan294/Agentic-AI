# ASSIGNMENT

#uv venv OR .venv\Scripts\active OR uv init .   run this command line 
#.env                                           create this file and generate api key
#uv add python-dotenv                           run this command line 
#uv add openai-agents                           run this command line 

from dotenv  import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

#/ Python Dotenv Package /  uv add python-dotenv  
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

#/ Connection With Your LLM / Learn Agentic AI Code Copy Paste
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
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

# / Openai Agents SDK / uv add openai-agents 
agent = Agent(
    name = "Translator Agent",
    instructions = "You are a helpful translator. Always translate English sentences into clear and simple Urdu"
)

response = Runner.run_sync(
    agent,
    input="My name is Muhammad Arsalan. I am an aspiring developer and AI learner with a strong " \
    "interest in building intelligent agents and language tools. I am currently working on a translator" \
    " agent that can assist users in translating text between different languages accurately and efficiently." \
    " I enjoy learning new technologies and applying them to real-world use cases..",
    run_config=config
)

# Print the translated result
print(response.final_output)

#uv run main.py
#jo bhi answer aye ga os ko copy kar ky notepad open kar ky paste karna hai




