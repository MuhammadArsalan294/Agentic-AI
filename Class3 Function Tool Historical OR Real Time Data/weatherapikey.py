from agents import Agent, Runner, function_tool
from main import config # import module ye main file sy import kia

import requests

@function_tool # Decorator lga kar function ko tool bna dia or upper es ko import bhi kia hai
def get_weather(city: str): # ye python function bnaya hai
    response = requests.get(f"https://wttr.in/{city}?format=3")
    print("-----API RESULT-----")
    print(response.text)
    return response.text  # real-time weather from wttr.in
    
# / Openai Agents SDK / uv add openai-agents 
agent = Agent(
    name = "Weather Agent",
    instructions = "You are a helpful assistant. Your task is to help the user with their queries",
    tools = [get_weather] # ye upper sy aya hai or yaha function ka name likha hai 
)

result = Runner.run_sync(
    agent,
    'What is the current weather in Karachi today?',
    run_config=config
)

print(result.final_output)

# uv run weatherapikey.py

"""
-----API RESULT-----
Karachi: ☁️   +28°C

The current weather in Karachi is 28 degrees Celsius with cloudy conditions.
"""