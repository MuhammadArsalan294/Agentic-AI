from agents import Agent, Runner
from main import config
import asyncio # Asynchronous input output

async def run_main():
    
    plant_agent = Agent(
        name="Plant Agent",
        instructions="You are a plant agent. Your task is to answer user query related to plants."
    )
    
    medicine_agent = Agent(
        name="Medicine Agent",
        instructions="You are a medicine agent. Your task is to answer user query related to medicines."
    )
   
    parent_agent = Agent(
        name="Parent Agent",
        instructions=
        "You are a parent agent. Your task is to delegate user queries to the appropriate agent. "
        "Delegate plant and flower related queries to the plant agent. "
        "Delegate medicine-related queries to the medicine agent. "
        "If the query is unrelated to plants or medicine, handle it yourself by refusing to answer.",
        handoffs=[plant_agent, medicine_agent] # handsoff ky parameter mein agents ky name pass hon gay jo hum ny agents bnayein hein
    )
    result = await Runner.run(
        parent_agent,
        "What is photosynthesis?",  # plant sy related query dy ga LLM sy
        #"What are red-blood cells", # medicine sy related query dy ga LLM sy 
        #"What are dictionaries in python?", # Ye query agent ky pass nhi hai kyu k hum ny agent nhi bnaya tw answer mein sorry kr dy ga
        run_config=config
    )
    
    print(result.final_output)
    print("Last Agent ==> ", result.last_agent)

if __name__ == "__main__": 
    asyncio.run(run_main())


#uv run handoffs.py  # Run this command line to execute the agent

# triage_agent means parent agent 
# hum ny multi agent bnaye jasey ky plant/medicine/parent agent then runner main hum ny parent pass kia or jis ko hum/user input/user input dety hain jasey ky medicine ki di tw wo LLM sy hamein sirf medicine sy related query la kar dy raha hai.

# Multi agent yani har agent ka apna apna task hoga. Yani har agent apne kam mein specialized hai. Jasey ky NIC ky liye gaye or waha aik table sy dusrey or dusrey sy tesrey / Doctor ky pass jana jasey ky phle counter sy hoty huye phir doctor tak jana 