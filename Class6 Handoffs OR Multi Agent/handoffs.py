from agents import Agent, Runner
from main import config
import asyncio # Asynchronous input output


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

async def run_main():
    result = await Runner.run(
        parent_agent,
        #"What is photosynthesis?",  # plant sy related query dy ga LLM sy
        #"What are red-blood cells", # medicine sy related query dy ga LLM sy 
        "What are dictionaries in python?", # Ye query agent ky pass nhi hai kyu k hum ny agent nhi bnaya tw answer mein sorry kr dy ga
        run_config=config
    )
    
    print(result.final_output)
    print("Last Agent ==> ", result.last_agent)
    #print("New Items",result.new_items)

if __name__ == "__main__": 
    asyncio.run(run_main())


# uv run handoffs.py 

"""
# triage_agent means parent agent 
# hum ny multi agent bnaye jasey ky plant/medicine/parent agent then runner main hum ny 
# parent pass kia or jis ko hum/user input dety hain jasey ky medicine ki di tw wo LLM 
# sy hamein sirf medicine sy related query la kar dy raha hai.

# Multi agent yani har agent ka apna apna task hoga. Yani har agent apne kam mein 
# specialized hai. Jasey ky NIC ky liye gaye or waha aik table sy dusrey or dusrey 
# sy tesrey / Doctor ky pass jana jasey ky phle counter sy hoty huye phir doctor tak jana.


"""

# Answer:
"""
Photosynthesis is how plants make their own food! It's a fascinating process where they use sunlight, water, and carbon dioxide to create sugars (their food) and oxygen (which we breathe!). Think of it like a plant's personal solar-powered food factory.

Last Agent ==>  Agent(name='Plant Agent', handoff_description=None, tools=[], mcp_servers=[], 
mcp_config={}, instructions='You are a plant agent. Your task is to answer user query related 
to plants.', prompt=None, handoffs=[], model=None, model_settings=ModelSettings(temperature=None, top_p=None, frequency_penalty=None, presence_penalty=None, tool_choice=None, parallel_tool_calls=None, truncation=None, max_tokens=None, reasoning=None, metadata=None, store=None, include_usage=None, response_include=None, extra_query=None, extra_body=None, extra_headers=None, 
extra_args=None), input_guardrails=[], output_guardrails=[], output_type=None, hooks=None, tool_use_behavior='run_llm_again', reset_tool_choice=True)
"""