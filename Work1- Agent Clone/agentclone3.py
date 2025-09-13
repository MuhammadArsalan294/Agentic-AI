from main import config
from agents import Agent, Runner, function_tool


###############  Cloning with Different Tools ###############


@function_tool
def calculate_area(length: float, width: float) -> str:
    """Calculate rectangle area"""
    return f"Area = {length * width} square units"


@function_tool
def get_weather(city: str) -> str:
    """Get weather for a city"""
    return f"Weather in {city}: Sunny, 72°F"


# Base agent with one tool
base_agent = Agent(
    name="BaseAssistant",
    instructions="You are a helpful assistant.",
    tools=[calculate_area]
)


# Clone with additional tool
# Weather + Math agent
weather_agent = base_agent.clone(
    name="WeatherAssistant",
    instructions="You are a weather and math assistant.",
    tools=[calculate_area, get_weather]   # New tools list
)


# Clone with different tools
math_agent = base_agent.clone(
    name="MathAssistant",
    instructions="You are a math specialist.",
    tools=[calculate_area]    # Same tools
)


# Test Queries 
query_area = "Please calculate the area of a rectangle with length 5 and width 3."
query_weather = "What is the weather in Lahore?"


# Run with base agent
result_base = Runner.run_sync(
    base_agent,
    query_area,
    run_config=config
)


# Run with weather agent
result_weather = Runner.run_sync(
    weather_agent,
    query_weather,
    run_config=config
)


# Run with math agent
result_math = Runner.run_sync(
    math_agent,
    query_area,
    run_config=config
)


# ---------- Print Results ----------
print("Base Agent:", result_base.final_output)
print("Weather Agent:", result_weather.final_output)
print("Math Agent:", result_math.final_output)


# uv run agentclone3.py

"""
Answer:

Base Agent: The area of the rectangle is 15.0 square units.

Weather Agent: The weather in Lahore is Sunny with a temperature of 72°F.

Math Agent: The area of the rectangle is 15 square units.

"""