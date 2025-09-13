from main import config
from agents import Agent, Runner
from pydantic import BaseModel
import asyncio

# Define your data structure
class PersonInfo(BaseModel):
    name: str
    age: int
    occupation: str

# Create agent with structured output
agent = Agent(
    name="InfoCollector",
    instructions="Extract person information from the user's message.",
    output_type=PersonInfo, #This is the magic    # output_type  ye he name likhein gay yaha agar change kia tw error aye ga
    #run_config=config                            # ye yaha bhi pass kr skty hain
)

async def main():
    result = await Runner.run(
        agent,
        "Hi, I'm Alice, I'm 25 years old and I work as a teacher.",
        run_config=config
    )

    # Now you get perfect structured data!
    print("Type:", type(result.final_output))        # <class 'PersonInfo'>
    print("Name:", result.final_output.name)         # "Alice"
    print("Age:", result.final_output.age)           # 25
    print("Job:", result.final_output.occupation)    # "teacher"


if __name__ == "__main__":
    asyncio.run(main())


# uv run structureoutput.py

"""
Answer:

Type: <class '__main__.PersonInfo'>
Name: Alice 
Age: 25     
Job: teacher

"""