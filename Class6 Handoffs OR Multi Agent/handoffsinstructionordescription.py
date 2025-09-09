from agents import Agent, Runner
from main import config
import asyncio
import rich
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX # hmein ye cose mila hai handoffs ky liye sdk ki trf sy hum use krein es ko

print(RECOMMENDED_PROMPT_PREFIX) # ye sdk ki trf sy dia hua prompt use kr rhy or print krwaya hai 


# Child Agent / Sub Agent 
billing_agent = Agent( # transfer_to_billing_agent agentsdk mere agent ka ye name rakhy ga yani agent ky name sy phle transfer_to lga dia
    name="Billing Agent",  
    instructions=f""" You are a billing agent. Your task is to assist users with billing-related inquiries and issues.""",
    handoff_description="""
    This is a billing agent. It handles user queries  # ye line new likhi hai jasey tool ki discription hoti thi asey sub agent ki bhi hoti hai ye code ko strong bnaye ga 
    related to billing."""# handoff_description hmarey child agent py apply hon gay. es main ye likhty hai ky jo agent hai wo kis purpose ky liye bana hua hai. yani ye sub agent ky notes hoty hain means documentation
)

# medicine_agent = Agent() # trasnfer_to_medicine_agent
# plant_agent = Agent()    # transfer_to_plant_agent

# Parent Agent
triage_agent = Agent(
    name="Triage Agent",
    instructions=f""" {RECOMMENDED_PROMPT_PREFIX} You  
    are a  triage agent. Your task is to delegate tasks
      to the appropriate specialized 
    agents based on the user's request.""", # {RECOMMENDED_PROMPT_PREFIX} ye f string m lgy ga or jaha handoffs hoga waha he lgy ga wasey kahi bhi lga skty hain
    handoffs=[billing_agent]
)

async def main():
    result = await Runner.run(
        triage_agent, # yani runner main jo define hoga wo first agent hoga os ko query jaye gi
        input="I have a question about my last invoice.",
        run_config=config,
    )
    
    rich.print(result.new_items)
    rich.print(result.final_output)
    rich.print(result.last_agent.name) # answer Billing Agent yani answer yaha sy a rha lekin es ny apna kam dusre agent ko dia hua hai means handoffs kr dia hai

if __name__ == "__main__":
    asyncio.run(main())

# uv run handoffsinstructionordescription.py

"""
# HandoffsCallItem ye class atti hai jab handoffs call hota hai tw

# handoffs ky case main openai agent sdk ki trf sy aik (RECOMMENDED_PROMPT_PREFIX) prompt dia gaya hai.Agent sdk ky developer khty hain ky handoffs 
# ki surat main context/prompt ko strong krna hai tw ap es chez ka use kro.
# yani instruction main ja kar (RECOMMENDED_PROMPT_PREFIX) lga do es sy LLM ko pura context mil jaye ga ky ye jo prompt/system prompt/input prompt/persona 
# likha gaya hai ye hand offs ky liye likha gaya hai

# OR

# Handoffs ke case me OpenAI Agent SDK ek RECOMMENDED_PROMPT_PREFIX deta hai. Developer recommend karte hain ke handoffs situation me context strong 
# karne ke liye is prefix ko instructions me use karo, taa ke LLM ko clear ho jaye ke yeh prompt specifically handoffs ke liye likha gaya hai.

"""