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
    tracing_disabled=True   # Yani trace nhi krey ga
)

# / Openai Agents SDK / uv add openai-agents 
agent = Agent(
    name="Writer Agent",
    instructions="Your task is to answer user query. If you do not have the answer to the user query just deny. Do not hallucinate.",# Why is an Agent considered stateless? Because it forgets past data after each execution
)

response = Runner.run_sync(
    agent,
    input = 'What is the next.js app router? ',
    run_config = config 
)
print(response)
#print(response.final_output)
#print(response.last_agent)

# uv run main.py

"""
Agents
Agents are the core building block in your apps. An agent is a large language model (LLM), 
configured with instructions and tools.

Basic configuration
The most common properties of an agent you'll configure are:

name: A required string that identifies your agent.
instructions: also known as a developer message or system prompt.
model: which LLM to use, and optional model_settings to configure model tuning parameters like temperature, top_p, etc.
tools: Tools that the agent can use to achieve its tasks.
"""
# Answer:
"""
RunResult:
- Last agent: Agent(name="Writer Agent", ...)
- Final output (str):
    The Next.js App Router is a new routing system in Next.js that replaces the Pages Router. 
 It offers a more streamlined, file-system-based routing approach with improved performance and features like server components and better support for React Server Components.
- 1 new item(s)
- 1 raw response(s)
- 0 input guardrail result(s)
- 0 output guardrail result(s)
(See `RunResult` for more details)
"""