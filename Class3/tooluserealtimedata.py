from agents import Agent, Runner, function_tool
from main import config # import module ye main file sy import kia

@function_tool # Decorator lga kar function ko tool bna dia or upper es ko import bhi kia hai
def usd_to_pkr(): # ye function bnaya hai
    return 'Today USD to PKR is Rs.280'

agent = Agent(
    name = "General Agent",
    instructions = "You are a helpful assistant. Your task is to help the user with their queries",
    tools = [usd_to_pkr] # ye upper sy aya hai or yaha function ka name likha hai 
)

result = Runner.run_sync(
    agent,
    'What is USD to PKR today?',
    run_config=config
)

print(result.final_output)

# uv run toolrealtimedata.py