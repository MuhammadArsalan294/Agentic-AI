from agents import Agent, Runner, function_tool 
from main import config
import requests
import rich # uv add rich 

#Creating a function as a tool which sends request to website API tp get products data
@function_tool
def get_products():
    url = "https://template-03-api.vercel.app/api/products"
    response = requests.get(url)
    return response.json()

#Creating Agent
agent = Agent(
    name = "Shopping Agent",
    instructions = """You are a smart shopping assistant 
    that helps users find, compare, and purchase products based on their preferences""",
    tools = [get_products]
)

#Runnig the agent
result = Runner.run_sync(
    agent, 
    input = "Show me all the product list ",
    run_config= config
)

#Multiple queries to test the agent
test_query = [
    "1) Show me all available products.",
    "2) Can you suggest me the best shoes to buy?",
    "3) What products can I buy right now?",
    "4) Suggest me the most best products you have.",
    "5) Can you display all items you have?"
   
]

#Looping through each query
for query in test_query:
    rich.print(f"\n[bold yellow]🧑 User Prompt:[bold yellow] {query}") #rich upper import kia hai libray sy OR yaha color set kia hai rich sy

    result = Runner.run_sync(
    agent , 
    input = query ,
    run_config= config
)
    
    rich.print(f"\n[bold green]Agent Response:")
    print(result.final_output)

# uv run shoppingagent.py