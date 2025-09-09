from agents import Agent, Runner, ModelSettings, function_tool
from main import config # import module ye main file sy import kia

@function_tool # Decorator lga kar function ko tool bna dia or upper es ko import bhi kia hai
def usd_to_pkr(): # ye python function bnaya hai
    return 'Today USD to PKR is Rs.280'

agent = Agent(
    name = "General Agent",
    instructions = "You are a helpful assistant. Your task is to help the user with their queries",
    tools = [usd_to_pkr], # ye upper sy aya hai or yaha function ka name likha hai # parameter

    # 2. Tool Choice - The "Can I Use Tools?" Switch
    #model_settings=ModelSettings(tool_choice="auto"), # Agent can decide when to use tools (default) # agent_auto tools ko apni marzi se use karega.Agar question tools ke bina answer ho jata hai, toh direct jawab dega.Agar question me calculation ya weather ka kaam ho, toh tool call karega.Default behavior auto hai.
    #model_settings=ModelSettings(tool_choice="required"), # Agent MUST use a tool (even if not needed) # agent_required ko hamesha tool use karna hi hoga.Even agar simple sawaal ho jaise "What is 2+2?", tab bhi wo calculator tool use karega.Matlab direct jawab dena allowed nahi hai.
    #model_settings=ModelSettings(tool_choice="none"), # Agent CANNOT use tools (chat only) # agent_no_tools ko tools ki access hi nahi hai.Ye sirf apne trained knowledge aur reasoning se jawab dega.Agar aap poochho "Weather in Lahore?", toh ye guess karega ya apna knowledge use karega, tool call nahi karega.

    # Parallel Tool Calls 
    #model_settings=ModelSettings(
    #    tool_choice="auto",
    #    parallel_tool_calls=True  # Use multiple tools simultaneously # # parallel_agent ek hi waqt multiple tools ek saath use kar sakta hai.
    #),
    #model_settings=ModelSettings(
    #    tool_choice="auto",
    #    parallel_tool_calls=False  # Use tools one by one # sequential_agent ek waqt me sirf ek tool call karega.
    #),
    
    # Top-P and Penalties
    #model_settings=ModelSettings(
    #    top_p=0.3,              # Use only top 30% of vocabulary # Model sirf top 30% most likely words me se choose karega.Matlab vocabulary zyada focused aur limited hogi.Example: Agar model ke paas 100 possible words hain, sirf top 30% probability wale consider karega.
    #   frequency_penalty=0.5,  # Avoid repeating words # Model ko penalize karega agar same word bar-bar repeat kare.Useful for cleaner, non-repetitive text.Example: Instead of "sun is bright, bright, bright", output hoga "sun is bright and warm".
    #   presence_penalty=0.3    # Encourage new topics # Encourage karta hai ke new topics ya new words use ho.Matlab agent thoda variety add karega instead of sticking to the same subject only.
    #)  
)

result = Runner.run_sync(
    agent,
    'What is USD to PKR today?', # argument
    run_config=config
)

print(result.final_output)

# uv run tooluserealtimedata.py

"""
# Tools
# Jab bhi humein Real Time Data / Current Information Chahiye ho kisi bhi cheez ki jasey ky
# Current Date, Currency Rate, Weather Update tw es ki current information LLM ky pass nahi 
# hoti wo Tool use kar ky hamein Current Information deta hai es ko Tool Callong kehty hain.

# Tool Caling Work
# Hum ny jo query likhi hai ye LLM ky pass Jaye gi or LLM khud sy dekhy ga agar wo answer 
# kar skta tw thik warna @function_tool decorator sy bana hua function call kar ky answer 
# dy ga.

# 1.Hosted Tools
#   ye use karne ky liye OPENAI kEY honi chahiye es ko free main use nhi kar skty.
#   Hosted Tools OPENAI ny hamein khud bana kar dy diye hain jasey ky
#   WebSearchTool,
#   FileSearchTool,
#   ComputerTool,
#   CodeInterpreterTool,
#   HostedMCPTool,
#   ImageGeneratorTool,
#   LocalShellTool,

# 2.Function Tools
#   Ye Python function ky tool hoty hain es ko hum use kar skty hain.Function ko Tool bana
#   kar jasey ky.
#   Function
#   API

# 3.Agents as Tools
#   Jasey hum ny Translator Agent banaya tha usy bhi hum Tool bana kar use kar skty hain.

"""
"""
Tools let agents take actions: things like fetching data, running code, calling external 
APIs, and even using a computer. There are three classes of tools in the Agent SDK:

1.Hosted tools: these run on LLM servers alongside the AI models. OpenAI offers retrieval, 
  web search and computer use as hosted tools.
2.Function calling: these allow you to use any Python function as a tool.
3.Agents as tools: this allows you to use an agent as a tool, allowing Agents to call other 
agents without handing off to them.
"""

# Answer:
"""
Today USD to PKR is Rs.280.
"""
