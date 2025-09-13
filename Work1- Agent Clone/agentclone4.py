from main import config
from agents import Agent, ModelSettings, Runner


###############  Multiple Clones from One Base ###############


# Create a base agent
base_agent = Agent(
    name="BaseAssistant",
    instructions="You are a helpful assistant.",
    model_settings=ModelSettings(temperature=0.7)
)


# Create multiple specialized variants
agents = {
    "Creative": base_agent.clone(
        name="CreativeWriter",
        instructions="You are a creative writer. Use vivid language.",
        model_settings=ModelSettings(temperature=0.9)
    ),
    "Precise": base_agent.clone(
        name="PreciseAssistant", 
        instructions="You are a precise assistant. Be accurate and concise.",
        model_settings=ModelSettings(temperature=0.1)
    ),
    "Friendly": base_agent.clone(
        name="FriendlyAssistant",
        instructions="You are a very friendly assistant. Be warm and encouraging."
    ),
    "Professional": base_agent.clone(
        name="ProfessionalAssistant",
        instructions="You are a professional assistant. Be formal and business-like."
    )
}


# Test all variants
query = "Tell me about artificial intelligence."


for name, agent in agents.items():
    result = Runner.run_sync(
        agent, 
        query,
        run_config=config
    )
    print(f"\n{name} Agent:")
    print(result.final_output[:100] + "...")



# uv run agentclone4.py

"""
Answer:

(Agent Clone) D:\AI-PYTHON-ASSIGNMENT\Agent Clone> uv run agentclone4.py

Creative Agent:
Ah, Artificial Intelligence. It's a term that conjures images of gleaming robots, futuristic landsca...

Precise Agent:
Artificial intelligence (AI) is the ability of a computer or machine to mimic human cognitive functi...

Friendly Agent:
Hello! I'd be happy to tell you about Artificial Intelligence (AI). It's a really exciting field!

A...

Professional Agent:
Artificial intelligence (AI) is a multifaceted field of computer science focused on creating machine...

"""