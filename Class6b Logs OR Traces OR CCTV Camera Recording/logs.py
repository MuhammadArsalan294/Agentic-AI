from agents import Agent, Runner, function_tool, trace # trace ko import kia agent ky module sy
from main import config
import asyncio # Asynchronous input output


@function_tool
def current_weather():
   return "Sunny"

@function_tool
def current_location():
   return "Governor House Karachi"

async def run_main():
    with trace("Class 06"): # with context management karta hai or trace wo function hai jo apko logs mein trace krey ga  "Class 06" logs ky work flow ky page py show hoga
          
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
            instructions="""  
            You are a parent agent. Your task is to
            delegate user query to approriate agent. and call the tool by yourself
            Delegate plant and flower related queries to plant agent.
            Delegate medicine related queries to medicine agent.
            Any query other than plant and medicine keep it to 
            yourself and deny the user query,

            You also have tools available like current location
            and current weather
            """,
            handoffs=[plant_agent, medicine_agent],  # handsoff ky parameter mein agents ky name pass hon gay jo hum ny agents bnayein hein
            tools=[current_location] # tools main function ky name pass hon gay
        )
        
        result = await Runner.run( # user prompt hota runner main
            parent_agent,
             """
                What are red-blood cells. and 
                what is my current location?
            """,  
            #"What is photosynthesis?",  # plant sy related query dy ga LLM sy
            #"What are red-blood cells?", # medicine sy related query dy ga LLM sy
            #"What is my current location?", 
            #"What are dictionaries in python?", # Ye query agent ky pass nhi hai kyu k hum ny agent nhi bnaya tw answer mein sorry kr dy ga
            run_config=config
        )

        print(result.final_output)
        print("Last Agent ==> ", result.last_agent.name)
        
if __name__ == "__main__": 
    asyncio.run(run_main())


#uv run logs.py # Run this command line to execute the agent

# Logs means tracess mtlb cid wale kia krty hain logs ka mtlb ye hota hai apki aplication ky upper kisi ny cctv camera lga dia hai cctv camera m kia hota hai ap jo bhi react krty hain wo cctv camera m record ho jata hai
# Logs ka mtlb bhi yehi hota hai apki screen/aplication main jo bhi ho rha hai wo kahi naw kahi capture/trace ho jaye Jasey insta m message ki api hai notification ki api hai or reels kii

# User input py asey likhne sy error aye ga
#"What is photosynthesis?",  
#"What is my current location"

# Ye thik tarika hai asey error nhi aye ga handsoff or tool dono chlein gay
# """" What are red-blood cells and 
#      what is my current location? """,


# Traces
# openai agents sdk search on google
# https://plateform.openai.com/docs
# Login/Signup
# Goto Dashboard OR Setting  from sidebar
# Click on Api key from sidebar
# Click on Create New Secret Key Copy 

# Paste the OPENAI_API_KEY in .env file
# Remove tracing _disabled=True from RunConfig
# Import python-dotenv in main.py

# sidebar click logs then trace on click