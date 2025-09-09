from main import config
from pydantic import BaseModel
from agents import( 
    Agent, 
    Runner, 
    RunContextWrapper, 
    function_tool, 
    trace
)
import asyncio
import rich

from dotenv import load_dotenv
load_dotenv()


class CartItems(BaseModel):
    product: list
    user_id: int
    brand: str
    total_amount: int

cart = CartItems(
    product=["Mobile", "Laptop"], 
    user_id="923021210812", 
    brand="apple", 
    total_amount=50000
)

async def MyPersonalFunction(wrapper: RunContextWrapper[CartItems]):
    return wrapper


@function_tool #function asynchronous/synchronous bhi ho skta or function tool bhi ho skta hai jis sy mera data LLM tak pohnchy ga
def products_info(wrapper: RunContextWrapper[CartItems]):
    print('Checking Context', wrapper)
    return f'{wrapper.context}'


def my_dynamic_instructions(context, agent): #ye function do parameter lazmi lein gay or return karna bhi lazmi ho ga
    return "You are a math teacher" # yaha wo system prompt/input aye ga jo instruction main likhty thy or aaj tak hum instruction string main dety thy but aaj function mein di hai dynamic instructions


personal_agent = Agent(
    name = "Agent",
    instructions= my_dynamic_instructions,# ye upper sy likha  # dynammic instructions ap ous waqt krty ho jab apko agent ky instruction ka parameter badlna ho ta ky ap apne agent ko situation or context ki awareness dy skko  
    tools = [products_info]   
)

async def main():
    with trace("Learn Dynamic Instructions"):
        result = await Runner.run(
            personal_agent, 
            'What is 10 + 10 * 3?', # User prompt/input
            run_config=config,
            context = cart #Local context
            )
        rich.print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())

# uv run agentcontext1.py

"""
#2.Agent/LLM Context – Public Data Store
#  Agent/LLM Context main public data store hota hai.Ye wo data hota hai jo tum deliberately 
#  LLM ko har baar provide karte ho.LLM ke paas visible hota hai, taky wo pichli baatein 
#  yaad rakhe./ wo data jo Agent/LLM ky pass available ho.
#  Example Use:Conversation history. Non-sensitive facts jo LLM ko future responses me 
#  kaam aayenge.

#  jab bhi agent/LLM context ki bat hogi hum ko do chezein zahn mein rakhni hain 
#  1.Dynamic instruction or 2. Conversion history

#1.Dynamic instruction 
#  Dynamic ka mtlb hai jo cheez change ho skti hai or instruction agent ko milty hain
#  Yani time ky sath instruction change hon jasey class m koi or kam or ghr ja kar koi or kam 

#  1.change according to the situation or 2.Context aware and personalized 

#  abhi tak hum static instructions use kar rahy thay static means change naw ho kuch bhi 
#  ho or ye string mein hoty thy
#  dynamic instructions wo hoty hain jo change ho skty hain or wo function asynchronous/synchronous 
#  bhi ho skty hain or function tool bhi ho skty hain.ye function do parameter lazmi lein gay or 
#  return bhi lazmi hongay.

#  jasey hum ny aik wesite bnai wo time ky hisab sy pakistan mein subha ky waqt 
#  good morning kahy gi or  USA mein es time ky hisab sy good afternoon kahy gi ye dynamic hai
#  OR aik ecommerce ki website hai ap chaty agar user login hai tw ousy payment krne do or 
#  buy krne do warna ousy kaho ap login nhi ho ap buy nhi kar skty ye jo chez hai ye hai 
#  context/situation awareness hai.

Dynamic instructions:
In most cases, you can provide instructions when you create the agent. 
However, you can also provide dynamic instructions via a function. 
The function will receive the agent and context, and must return the prompt. 
Both regular and async functions are accepted.
"""

"""
Answer:
Okay, let's solve this using the order of operations (PEMDAS/BODMAS). Multiplication comes before addition.

So, first we calculate 10 * 3 = 30

Then, we add 10 to the result: 10 + 30 = 40

Therefore, 10 + 10 * 3 = 40
"""
