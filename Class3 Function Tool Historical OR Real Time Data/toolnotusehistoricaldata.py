from agents import Agent, Runner
from main import config # import module ye main file sy import kia

# / Openai Agents SDK / uv add openai-agents 
agent = Agent(
    name = "General Agent",
    instructions = "You are a helpful assistant. Your task is to help the user with their queries"
)

result = Runner.run_sync(
    agent,
    'Who is the founder of Pakistan', # Historical Data
    #'What is the conversion rate of USD to PKR', # Real time data ye answer nhi dy ga sorry kr ly ga ya purana data dy ga  answer k liye humein tool calling ka use krna hoga
    #'Show me the top 10 student of class 10', # Personalised data ye answer nhi dy ga sorry kr ly ga ya purana data dy ga  answer k liye humein tool calling ka use krna hoga
    run_config=config
)

# Print the translated result
print(result.final_output)

# uv run toolhistoricaldata.py