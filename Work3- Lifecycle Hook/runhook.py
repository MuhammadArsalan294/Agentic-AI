from agents import Agent, Runner, RunHooks, RunContextWrapper, function_tool, Tool
from main import config
import asyncio
from typing import Any


class MyRunHooks(RunHooks):

    async def on_agent_start(self, context: RunContextWrapper, agent: Agent) -> None:
        """Called before the agent is invoked. Called each time the current agent changes."""
        print("Start Run")
        print("Start Agent Name:", agent.name) # pura agent bhi a skta hai yaha 
      

    async def on_agent_end(self, context: RunContextWrapper, agent: Agent, output: Any) -> None:
        """Called when the agent produces a final output."""
        print("End Run")
        print("End Agent Name:", agent.name)
  


    async def on_tool_start(self, context: RunContextWrapper, agent: Agent, tool: Tool) -> None:
        """Called concurrently with tool invocation."""
        print("Start Tool Run")
        print("Start Agent Name:", agent.name)
        print("Start Tool Parameter:", tool)


    async def on_tool_end(self, context: RunContextWrapper, agent: Agent, tool: Tool, result: str) -> None:
        """Called after a tool is invoked."""
        print("End Tool Run")
        print("End Agent Name:", agent.name)
        print("End Tool Parameter:", tool)


    async def on_handoff(self, context: RunContextWrapper, from_agent: Agent, to_agent: Agent) -> None:
        """Called when a handoff occurs."""
        print("Run Handoff ")
        print("From Agent Name:", from_agent.name) # from_agent asey bhi kar skty
        print("To Agent Name:", to_agent.name)
   

@function_tool
def plus(n1: int, n2: int):
    """Plus function"""
    print("Plus Tool Fire ---->")
    return n1+n2


math_assistant = Agent(
    name="Math Assistant",
    instructions="You are a helpful math teacher",
    handoff_description="This is a good math teacher",
    tools=[plus]
)

assistant = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    handoffs=[math_assistant]
)

async def main():
    res = await  Runner.run(
        starting_agent= assistant,
        input="2+2=?",
        run_config=config,
        hooks=MyRunHooks()
    )
    print(res.final_output)

if __name__ == "__main__":
    asyncio.run(main())


# uv run runhook.py


"""

Key Points for Beginners 📚:
Setup: Use run_hooks=YourHooksClass() in the run() function



❌ Don't Do This:
# Confusing run hooks with agent hooks
agent.hooks = RunHooksBase()  # Wrong! Use AgentHooksBase for agents

# Forgetting to pass run_hooks to run()
result = run(agents=agent1)  # No monitoring!

####################################################################

✅ Do This Instead:
# Correct setup for run hooks
system_monitor = MyRunHooks()
result = await run(
    agents=agent1 
    run_hooks=system_monitor  # Correct!
)

# Agent hooks are separate
agent1.hooks = MyAgentHooks()  # Individual agent monitoring
"""