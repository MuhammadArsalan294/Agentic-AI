from main import config
from agents import Agent, Runner, function_tool


############### Understanding Shared References ###############


# Tools
@function_tool
def calculate_area(length: float, width: float) -> str:
    """Calculate rectangle area"""
    return f"Area = {length * width} square units"


# Demonstrate shared references
original_agent = Agent(
    name="Original",
    instructions="You are helpful.",
    tools=[calculate_area], # new_tool, ye bhi a gaya tool yaha
)


# Clone without new tools list
shared_clone = original_agent.clone(  # original_agent ko clone kia tw yaha bhi do tool ho gaye. agar es main tools= ka parameter dalty tw wo count hota
    name="SharedClone",
    instructions="You are creative."
)


# Add tool to original
@function_tool
def new_tool() -> str:
    return "I'm a new tool!"


original_agent.tools.append(new_tool)


# Check if clone also got new tool 
print("Original tools:", len(original_agent.tools))   # Expect 2
print("Shared clone tools:", len(shared_clone.tools)) # Expect 2 (shared reference!)


# Create independent clone
independent_clone = original_agent.clone(  
    name="IndependentClone",
    instructions="You are independent.",
    tools=[calculate_area],  # Fresh new list ,yaha original_agent ka tool es liye count nhi kiye kyu ky yaha tools= dia hua hau or ye 1 count hoga
)


# Add again to Original
original_agent.tools.append(new_tool) 


# Check Independent Clone 
print("Original tools after second append:", len(original_agent.tools))       # Expect 3
print("Independent clone tools:", len(independent_clone.tools))               # Expect 1 (independent!)


# uv run agentclone5.py

"""
Answer:

Original tools: 2
Shared clone tools: 2
Original tools after second append: 3
Independent clone tools: 1

"""