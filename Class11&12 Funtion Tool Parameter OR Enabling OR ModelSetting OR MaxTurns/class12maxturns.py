from main import config
from agents import Agent, ModelSettings, Runner, function_tool
import asyncio
import rich


#################### Max Turns ####################

@function_tool(
        name_override="add_numbers",
        description_override="Add two numbers together and return the result.",
        # is_enabled=True
        # is_enabled=False 
        )
def add(a: int, b: int) -> int:
    """
    Add two numbers.
    """
    return a + b 

@function_tool
def subtract(a: int, b: int) -> int:
    """
    Subtract two numbers.
    """
    return a - b

math_agent = Agent(
    name="Math Agent",
    instructions=""" You are a math agent. Your task is to assist users with math-related inquiries and calculations.""",
    tools=[add, subtract],
    model_settings=ModelSettings(
        # tool_choice="auto"
        # tool_choice="required"
        # tool_choice="none"
    )
)


async def main():
    result = await Runner.run(
        math_agent,
        input="What is 5 plus 3?",
        run_config=config,
        max_turns=2, #  OK
        #max_turns=1, #  Error MaxTurnExceeded # max_turns=1 py error aye ga or ye 2 ya 2 sy zyada honi chahiye 12 bhi ho skti or es ki default value 10 hai 
    ) 
    rich.print(result.new_items)
    rich.print(result.final_output)
    rich.print(result.last_agent.name)

if __name__ == "__main__":
    asyncio.run(main())

# uv run maxturns.py

"""
# LLM hmari query ko analyse karta hai phir jawab deta hai or jawab string main deta hai final_output or function tool call kar ky jawab dy skta 
# or handoffs kar ky bhi jawab dy skta hai.
# agar function /tool call hoga tw sab sy phle json return krta hai LLM yani json jaye gi LLM ky pass or LLM ko pta hai mjhe json main jawab 
# nhi dena string main dena hai.
# jab aik tool call hota hai os ky jo turns hoty hain wo 2 hoty hein.
# first turn mein LLM json return karta hai or second turn main jawab deta hai.
# agar hum max_turns=1 krein gay tw error aye ga or max_turns=2 ya es sy zyada hone chahiye or es ki deafault value max_turns=10 hai

# LLM analyze the query then LLM replies.
# 1.It may a string final_output
# 2.It may a call a function/tool
# 3.It may handoffs
"""