from dotenv  import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
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
