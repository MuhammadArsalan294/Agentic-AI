from agents import Agent, Runner, AgentHooks, RunContextWrapper, function_tool, Tool
from main import config
from typing import Any
import asyncio


# Custom AgentHooks subclass
class MyAgentHooks(AgentHooks): # cntrl plus (AgentHooks) clicks tw hooks open # Aapne ek custom hooks class banayi jo AgentHooks ko inherit karti hai.inherit mtlb jo AgentHooks main wo he MyAgentHook main bhi a gaya
     
    async def on_start(self, context: RunContextWrapper, agent: Agent) -> None: # self → matlab ye function MyAgentHooks class ke andar hai (ye default hota hai). # context: RunContextWrapper → isme running ke time ka environment hota hai (jaise agent ki history, input,output, config waghera). # agent: Agent → ye batata hai kaunsa agent start hua hai (Assistant ya Math Assistant). # -> None → ye function kuch return nahi karega, sirf action karega (yaha print).
        """Called before the agent is invoked. Called each time the running agent is changed to this
        agent.""" # # Jab bhi hmara agent start hoga ye chly ga or ye aik function hai 
        print("Start Agent ")
  
        
    async def on_end(self, context: RunContextWrapper, agent: Agent, output: Any) -> None: # # agent: Agent → ye batata hai kaunsa agent end hua hai (Assistant ya Math Assistant). output: Any → agent ne jo final result banaya hai, woh yaha milta hai. 
        """Called when the agent produces a final output."""  # Jab bhi hmara agent end hoga ye chly ga or ye aik function hai 
        print("End Agent")


    async def on_tool_start(self, context: RunContextWrapper, agent: Agent, tool: Tool) -> None: #agent: Agent → kaunsa agent ye tool use kar raha hai.tool: Tool → kaunsa tool chal raha hai (yaha plus).
        """Called concurrently with tool invocation."""  # tool chalne se pehle ye chly ga.
        print("Start Tool Hook")


    async def on_tool_end(self, context: RunContextWrapper, agent: Agent, tool: Tool, result: str) -> None: # result: str (sirf on_tool_end mein) → tool ne kya result diya. ye tool end hone ky bad chly ga jab tool result dy dy ga os ky bad print hoga
        """Called after a tool is invoked.""" # tool chalne ke baad ye chly ga. 
        print("End Tool Hook")

    
    async def on_handoff(self, context: RunContextWrapper, agent: Agent, source: Agent) -> None: #agent: Agent → wo agent jo kaam receive kar raha hai.source: Agent → wo agent jo kaam handoff kar raha hai (de raha hai).
        """Called when the agent is being handed off to. The `source` is the agent that is handing # ek agent dusre agent ko kaam dega to “Handoff Hook”.
       off to this agent."""
        print("Handoff Hook")



@function_tool
def plus(n1: int, n2: int):
    """Plus function"""
    print("Plus Tool Fire ---->")
    return n1+n2


math_assistant = Agent(
    name="Math Assistant",
    instructions="You are a helpful Teacher",
    hooks=MyAgentHooks(), # hooks ka parameter hai phir hmara bnai hui class pass ki 
    #tools=[plus]
)

assistant = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    hooks=MyAgentHooks(), # hooks ka parameter hai phir hmara bnai hui class pass ki 
    tools=[plus],
    handoffs=[math_assistant]
)

async def main():
    res = await  Runner.run(
        starting_agent= assistant,
        input="2+2=?",
        run_config=config
    )
    print(res.final_output)

if __name__ == "__main__":
    asyncio.run(main())

# uv run agenthook.py

"""
Lifecycle events (hooks)
Hooks / Event do trha ky hoty hain aik wo hoty hain jo agent ky sath chlty hain or dusrey wo hoty jo runner ky sath chlty hain


Lifecycle events (hooks)
Sometimes, you want to observe the lifecycle of an agent. For example, you may want to log events, or pre-fetch data when certain events occur. You can hook into the agent lifecycle with the hooks property. Subclass the AgentHooks class, and override the methods you're interested in.

Key Points for Beginners 📚:
Async: All hook methods must be async functions
Attachment: You attach hooks using agent.hooks = YourHooksClass()
Funtion name same rakhein gay agar  on_start ye funtion name hai hum start function name rakh dety tw ye wala function nhi chly ga baki print hoga

"""
"""
❌ Don't Do This:
# Forgetting async
def on_start(self, context, agent):  # Missing 'async'!
    print("Started")

# Trying to return values from hooks
async def on_tool_end(self, context, agent, tool, result):
    return "modified result"  # Hooks don't return values!

############################################################
    
✅ Do This Instead:
async def on_start(self, context, agent):  # Proper async
    print("Started")

async def on_tool_end(self, context, agent, tool, result):
    # Just observe and log, don't try to modify
    print(f"Tool {tool.name} returned: {result}")


"""