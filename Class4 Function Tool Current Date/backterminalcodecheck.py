from agents import Agent, Runner, function_tool # funtion tool agent k module sy a rha hi
from main import config # import module ye main file sy import kia
from datetime import datetime
import rich # uv add rich terminal py  output read able krne k liye use krty hain ye or ye libray sy import kia hai

@function_tool # jitne bhi function bnao gay untny he decorator bhi lgao gy
def get_weather(city:str)->str:
    return f"the weather of {city} is rainy"

@function_tool#Decorator bhi function hoty hein  Decorator lga kar function ko tool bna dia or upper es ko import bhi kia hai
def get_date(): # ye simple function bnaya hai
    _now = datetime.now() # now means abhi
    return _now.strftime("the date is %d-%m-%Y")

@function_tool
def multiply(num1: int, num2: int)->int: # Parameter
    return num1 * num2  

# / Openai Agents SDK / uv add openai-agents 
agent = Agent( 
    name = "Assistant", # ye required parameter hai
    instructions = "You are a helpful assistant.",
    tools = [get_date, get_weather, multiply] # ye upper sy aya hai or yaha function ka name likha hai 
)

result = Runner.run_sync(
    agent,
    '5 multiply by 10', # pompt / augruments
    run_config=config
)

rich.print(result.new_items) # jasey run_sync sy final_output ata hai asey he new_items bhi hai
print(result.final_output) #final ouput string mein return krey ga means answer string mein dy ga

# uv run backterminalcodecheck.py

# hmarey jitne bhi function hain wo function tool return kr rha hai OR json form main a rhi hai properties/parameter LLM sy
# LLM ky pass query gai os ny parameter ko extract kia or json form mein extract krey ga parameter ko or json return hogi jo LLM ny function chosee kia hoga osko kaha sy mere prompt mein sy
#                                                  OR
# hmara Query LLM ky pass jaye gi JSON form mein kha sy hmara function mein sy jo Function tool return kar rha hai