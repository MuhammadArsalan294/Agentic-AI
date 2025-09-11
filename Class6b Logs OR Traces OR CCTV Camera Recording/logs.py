from agents import Agent, Runner, function_tool, trace # trace ko import kia agent ky module sy
from main import config
import asyncio # Asynchronous input output

@function_tool
def current_weather():
   return "Sunny"

@function_tool
def current_location():
   return "Governor House Karachi"


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


async def run_main():
    with trace("Class 06"): # with context management karta hai or trace wo function hai jo apko logs mein trace krey ga  "Class 06" logs ky work flow ky page py show hoga
           
        result = await Runner.run( # user prompt hota runner main # yaha bhi user input f string mein use kar skty hain
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
        #print(f"Both: {result.final_output}") # ye dono f string ky sath bhi use kar skty 
       
        
if __name__ == "__main__": 
    asyncio.run(run_main())


# uv run logs.py 


# Logs means tracess mtlb cid wale kia krty hain. Logs ka mtlb ye hota hai apki aplication 
# ky upper kisi ny cctv camera lga dia hai cctv camera m kia hota hai ap jo bhi react krty
# hain wo cctv camera m record ho jata hai.
# Logs ka mtlb bhi yehi hota hai apki screen/aplication main jo bhi ho rha hai wo kahi naw
# kahi capture/trace ho jaye Jasey insta m message ki api hai notification ki api hai or
# reels kii

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


# Answer:
"""
Okay, I can help you with the red blood cell question!

**Red Blood Cells (Erythrocytes)**

Red blood cells are the most common type of blood cell and their main job is to carry oxygen from your lungs to the rest of your body. They also help carry carbon dioxide back to your lungs to be exhaled.

Here's a breakdown of their key features:

*   **Shape:** They have a unique biconcave disc shape (like a flattened donut with a shallow 
dip in the middle). This shape maximizes their surface area for oxygen absorption and makes them flexible enough to squeeze through tiny blood vessels.
*   **Hemoglobin:** Red blood cells are packed with a protein called hemoglobin. Hemoglobin binds to oxygen in the lungs and releases it in the tissues. It also binds to carbon dioxide. Hemoglobin is what gives red blood cells their red color.
*   **No Nucleus (in mammals):** Mature red blood cells in mammals don't have a nucleus or other organelles. This makes more space for hemoglobin, allowing them to carry more oxygen.      
*   **Production:** Red blood cells are produced in the bone marrow.
*   **Lifespan:** They have a lifespan of about 120 days. Old or damaged red blood cells are removed from circulation by the spleen and liver.

I am an AI and do not have a physical location.

Last Agent ==>  Medicine Agent
"""

"""MCQS
Debugging and observing step-by-step execution of agents

If tracing is enabled, what will you see in logs?
a) Function name, inputs (4,5), and result 20
"""