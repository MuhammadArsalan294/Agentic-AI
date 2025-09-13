from agents import Agent, Runner, AgentHooks, RunContextWrapper, function_tool, Tool
from main import config
from typing import Any
import asyncio
import requests


# Custom AgentHooks subclass
class MyAgentHooks(AgentHooks): # cntrl plus (AgentHooks) clicks tw hooks open
     
    async def on_start(self, context: RunContextWrapper, agent: Agent) -> None:
        """Called before the agent is invoked. Called each time the running agent is changed to this
        agent."""
        print("Start Agent ")
        print("Start Agent Name:",agent.name) # asey agent ka name btaye ga
        print("Start Context:", context.context)  # nechy wala context print krwaya hai
        #context.context["name"] = "Baber" # Yani nechy context main add kar dy ga ye bhi
        url = f"https://jsonplaceholder.typicode.com/users/{context.context["id"]}"
        res = requests.get(url)
        result = res.json()
        context.context["obj"] = result # yani user ka jo bhi data hai url main wo 'obj' ky bad likh do

        
    async def on_end(self, context: RunContextWrapper, agent: Agent, output: Any) -> None:
        """Called when the agent produces a final output."""  # Jab bhi hmara agent end hoga ye wala hook chly ga ye hook kia hai aik function hai
        print("End Agent")
        print("End Agent Name:", agent.name) # asey agent ka name btaye ga
        print("End Context:", context.context)


@function_tool
def plus(n1: int, n2: int):
    """Plus function"""
    print("Plus Tool Fire ---->")
    return n1+n2


assistant = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    hooks=MyAgentHooks(), # hooks ka parameter hai phir hmara bnai hui class pass ki 
)

async def main():
    res = await  Runner.run(
        starting_agent= assistant,
        input="2+2=?",
        run_config=config,
        context={"id": "3"}
    )
    print(res.final_output)

if __name__ == "__main__":
    asyncio.run(main())

# uv run agenthook1.py




