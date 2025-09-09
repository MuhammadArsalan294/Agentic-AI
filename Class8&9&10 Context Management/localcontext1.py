from main import config
from pydantic import BaseModel # BaseModel  parent class hogi
from dataclasses import dataclass
from agents import(
    Agent,
    Runner,
    RunContextWrapper, # ye agents ky module sy import hoga
    function_tool
)
import asyncio
import rich 

# You create any Python object you want. A common pattern is to use a dataclass or a Pydantic object.
class UserInfo(BaseModel): # jab bhi child class ky round bracket main kisi dusri class ka name ho wo concept inheritance khlata hai Yani parrent class main child class or jo bhi parent class m feature hon gay wo child main bhi a jayein gay  or Class ky name ka phla word hmesha bara aye ga yani Capital 
    user_id: int | str # yani user id integer bhi ho skti or string bhi
    name: str
# OR
#@dataclass
#class UserInfo:  
#    user_id: int | str
#    name: str

# create a class 
user = UserInfo(
    user_id = 12345,
    name = "Muhammad Arsalan"
) 


@function_tool # Yaha function_tool es liye banaya kyu ky mera jo Local Context hota hai wo mere code m available hota hai. Wo function_tool / handoffs / agent life cycle hooks main bhi available hota hai   # function asynchronous/synchronous bhi ho skta or function tool bhi ho skta hai jis sy mera data LLM tak pohnchy ga
def get_user_info(wrapper: RunContextWrapper[UserInfo]): # wrapper parameter hai or RunContextWrapper eik class hai es class ki bhi aik class/type hai UserInfo or [UserInfo] es ko generics khty hain generic means aik asi chez jo register nhi wo kisi ky sath bhi adjust ho jaye os ko koi bhi use kar ly jasey water generic hai
    #rich.print(wrapper)
    #rich.print(wrapper.context)
    #rich.print(wrapper.context.name) # single key return
    return f'The user info is {wrapper.context}' # pura object return


personal_agent = Agent(
    name = "Personal Agent",
    instructions="You are a helpful assistant, always call the tool to get user's information", # ye static instruction hai static ka mtlb hai wo chez jo kbhi bhi change nhi hoti # system prompt/input
    tools = [get_user_info]
)

async def main():
    result = await Runner.run( # Runner do kam karty hain runner agent ko execute karty hain or dusra apky code ko context provide karna 
        starting_agent = personal_agent,
        input = 'What is my name and also tell me my user id',  # ye wo question hai jis ka jawab mere LLM ky pass nhi hai Or jab sawal ka jawab nhi hota LLM ky pass tw wo function calling karta hai # User prompt/input
        run_config = config,
        context = user # Ye Local Context Ha yani private hai ye ye LLM ko available nhi hota # ye code m available hota hai or upper function call m available hai RunContextWrapper ki class m
    )
    rich.print(result.final_output)



if __name__ == "__main__":
    asyncio.run(main())

# uv run localcontext1.py


"""
# Context Management ka mtlb hai purani information ko yad rakho.
# Context ka mtlb hota hai background information/ knowledge. Background information ka mtlb kal cricket match hai 
# pakistan ka os ky barey main pta tw background information hai or agar nhi pta tw background information nhi hai.

# Management ka mtlb jo chezein yad hain ous ko sahi sy yad rakho / management ka mtlb hai kisi bhi chez 
# ko apne pass store karna ya dekhbhal krna

Context management:
Context available locally to your code: this is data and dependencies you might need when tool functions run,
during callbacks like on_handoff, in lifecycle hooks, etc.
Context available to LLMs: this is data the LLM sees when generating a response.
"""


"""
# Hum apni agentic applicatin mein agent sy bat karty hain or hmara agent LLM sy bat karta hai or jo LLM model 
# hoty hain wo stateless hoty hain .Stateless means yani agr ap ous sy koi bhi bat krein wo agli bar ous ko bhol 
# jaye ga. Yani jis request py hum os ky pass apna data ly kar gaye os ko bas wo he yad hai wo purana kuch b yad
# nhi rakhta. Hamein agent ko context deney ki es liye need hoti hai ta ky agent hmari purani batein yad rakh
# sakey or hmari bat agay bhar skey kyu ky jo LLM jo hoty hein wo stateless hoty hain. inko statefull kasey bana
# skty hein inko statefull bnany ki two type hoti hain ta ky wo purani batein/purana data yad rakh sakein.
# 1.Local context or  
# 2.Agent/LLM context

# 1.Local Context – Private Data Store / Personal Data
#   Local context main private data store hota hai jo LLM ko directly nazar nhi ata tum decide karty ho ky ismein 
#   sy konsi cheez LLM ko bhejni hai or konsi nhi bhejni. Yani wo data jo LLM tak nhi pohanchta ye sirf hmarey code 
#   base tak rahta hai or os data ko hum apne pass kasey get kar skty hein RunContextWrapper ki class sy ya khud sy 
#   bnaya hua koi bhi function/function_tool/handoffs ho waha sy mil jaye ga hmein RunContextWrapper/local context.
#   Example Use: (bank balance, password, private notes) User ka personal record jo sirf tumhare server ko pata ho.
 
Local context:
This is represented via the RunContextWrapper class and the context property within it. The way this works is:

You create any Python object you want. A common pattern is to use a dataclass or a Pydantic object.
You pass that object to the various run methods (e.g. Runner.run(..., **context=whatever**)).
All your tool calls, lifecycle hooks etc will be passed a wrapper object, RunContextWrapper[T], where T represents 
your context object type which you can access via wrapper.context.
The most important thing to be aware of: every agent, tool function, lifecycle etc for a given agent run must use 
the same type of context.

Note:
The context object is not sent to the LLM. It is purely a local object that you can read from, write to and
call methods on it.
"""

"""
Answer:
Your name is Muhammad Arsalan and your user ID is 12345.
"""