from main import config
from pydantic import BaseModel
from agents import( 
    Agent, 
    RunContextWrapper, 
    Runner, 
    function_tool, 
    trace
)
import asyncio
import rich

from dotenv import load_dotenv
load_dotenv()

# ------------------ Example of Local Context ------------------ #

class CartItems(BaseModel):
    product: list
    user_id: int
    brand: str
    total_amount: int

cart = CartItems(
    product=["Mobile", "Laptop"], 
    user_id="923021210812", 
    brand="apple", 
    total_amount=50000
)

async def MyPersonalFunction(wrapper: RunContextWrapper[CartItems]):
    return wrapper

@function_tool
def products_info(wrapper: RunContextWrapper[CartItems]):
    print('Checking Context', wrapper)
    return f'{wrapper.context}'


personal_agent = Agent(
    name = "Agent",
    instructions= "You are a Science Teacher",# system prompt/input
    tools = [products_info]
)


async def main():
    with trace("Learn Local Context"):
        result = await Runner.run(
            personal_agent, 
            'What is light?', # User prompt/input
            run_config=config,
            context = cart #Local context
            )
        rich.print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())

# uv run localcontext2.py

"""
Answer:
Light is a form of electromagnetic radiation that is visible to the human eye. It is a type of energy that travels in 
waves and can be emitted by objects that are heated or that undergo certain chemical or physical processes.

"""