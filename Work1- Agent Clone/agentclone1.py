from main import config
from agents import Agent, ModelSettings, Runner


############### Basic Cloning ###############


# Base agent
base_agent = Agent(
    name="BaseAssistant",
    instructions="You are a helpful assistant.",
    model_settings=ModelSettings(temperature=0.7)
)


# Simple clone
friendly_agent = base_agent.clone(
    name="FriendlyAssistant",
    instructions="You are a very friendly and warm assistant."
)


# Test both agents
query = "Hello, how are you?"


result_base = Runner.run_sync(
    base_agent, # agar dono agent la result chhahiye ye bhi aye ga agar ye yaha sy remove kia tw bas nechy wale ka answer dy ga # or yaha upper jo do agent bnayein hain wo dono nhi likh sktey aik he aye ga
    friendly_agent,
    query,
    run_config=config
)


result_friendly = Runner.run_sync(
    friendly_agent,  #  agar dono agent la result chhahiye tw ye bhi aye ga 
    query,
    run_config=config
)


print("Base Agent:", result_base.final_output)
print("Friendly Agent:", result_friendly.final_output)

# uv run agentclone1.py

# upper do agent banye hain tw agar dono agent sy result chaiye tw phir do runner bnana hon gay agr hum aik runner bnayein gay tw wo aik he agent bhi answer krey ga or dusra nhi

"""
Answer:

Base Agent: I am doing well, thank you for asking! How are you today?

Friendly Agent: Hello there! I'm doing wonderfully, thank you for asking! It's always a pleasure to connect with someone new. How are you doing today? Is there 
anything I can help you with? 😊

"""