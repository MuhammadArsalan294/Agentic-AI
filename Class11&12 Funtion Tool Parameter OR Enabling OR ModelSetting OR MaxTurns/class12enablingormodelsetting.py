from main import config
from agents import Agent, ModelSettings, Runner, function_tool
import asyncio
import rich


#################### Tool Enabling  OR ModelSetting Check Code ####################

@function_tool(
        name_override="add_numbers",
        description_override="Add two numbers together and return the result.",
        #is_enabled=False,
        #is_enabled=True,
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
        #tool_choice="auto",
        #tool_choice="required",
        #tool_choice="none"
    )
)

async def main():
    result = await Runner.run(
        math_agent,
        input="What is 5 plus 3",
        run_config=config,
    )
    rich.print(result.new_items)
    rich.print(result.final_output)
    rich.print(result.last_agent.name)

if __name__ == "__main__":
    asyncio.run(main())

# uv run class12enablingormodelsetting.py  


"""
⚙️is_enabled=True  or   tool_choice="none"

Input:
"What is 5 plus 3"

Tools available:
add ✅ enabled
subtract ✅ enabled

Agent setting:
tool_choice="none" → iska matlab
Agar model chahe to tool call kare, warna apne hi answer text mein de de.

"""

"""
⚙️is_enabled=False  or   tool_choice="required"

Input:
"What is 5 plus 3"

Tools available:
add ❌ disabled (is_enabled=False)
subtract ✅ enabled

Agent settings:
tool_choice="required" → tool call zaroor hoga

Execution:
Agent ko add use karna chahiye tha, lekin wo disabled hai →
Is liye agent subtract(5, 3) call karega.
"""