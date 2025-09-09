from agents import Agent, Runner, function_tool # funtion tool agent k module sy a rha hi
from main import config # import module ye main file sy import kia
from datetime import datetime


@function_tool # jitne bhi function bnao gay untny he decorator bhi lgao gy
def get_weather(city:str)->str:
    return f"the weather of {city} is rainy"

@function_tool#Decorator bhi function hoty hein  Decorator lga kar function ko tool bna dia or upper es ko import bhi kia hai
def get_date(): # ye function bnaya hai
    _now = datetime.now() # now means abhi
    return _now.strftime("the date is %d-%m-%Y")


# / Openai Agents SDK / uv add openai-agents 
agent = Agent( 
    name = "Assistant", # ye required parameter hai
    instructions = "You are a helpful assistant.",
    tools = [get_weather, get_date] # ye upper sy aya hai or yaha function ka name likha hai 
)

result = Runner.run_sync(
    agent,
   'Tell me the current date and time, and tell me weater of karachi, and what is my current location',# upper current locaton ka function  nhi bnaya
   run_config=config
)

print(result.final_output) #final ouput string mein return krey ga means answer string mein dy ga

# uv run realtimedatacurrentdate.py

# Answer:
"""
OK. Today is 01-09-2025 and the weather in Karachi is rainy. I still don't know your current location.
"""