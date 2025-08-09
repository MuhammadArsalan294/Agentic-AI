from main import config
from pydantic import BaseModel

from agents import (
    Agent,
    Runner, 
    output_guardrail,
    GuardrailFunctionOutput,  # ✅ class for guardrail output
    OutputGuardrailTripwireTriggered,
) 
import asyncio



class MessageOutput(BaseModel): # Model for Agent Output Type
    response: str

class PHDOutput(BaseModel): 
    response: str
    isPHDLevelResponse: bool

phd_guardrail_agent = Agent(
    name = "PHD Guardrail Agent",
    instructions="""
    You are a PHD Guardrail Agent that evaluates if text is too complex for 8th grade students. If the response if 
    very hard to read for an eight grade student deny the agent response
    """,
    output_type=PHDOutput
)

@output_guardrail
async def PHD_guardrail(ctx, agent: Agent, output) -> GuardrailFunctionOutput:

    result = await Runner.run(
        phd_guardrail_agent, 
        output.response,  
        run_config=config
    )
    

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered= result.final_output.isPHDLevelResponse
    )


# Main executor agent
eigth_grade_std = Agent(
    name = "Eight Grade Student",
    instructions="""
        1. You are an agent that answer query to a eight standard student. Keep your vocabulary simple and easy. 
        2. If asked to give answers in most difficult level use the most hardest english terms
    """,
    output_type=MessageOutput,
    output_guardrails=[PHD_guardrail]
)

async def og_main():
    #query = "What are trees? Explain using the most complex scientific terminology possible" # True
    query = "What are trees? Explain in simple words" # False
    try:
        result = await Runner.run(
            eigth_grade_std, 
            query, 
            run_config=config
        )

        print(result.final_output) # False 
        # Output: response='Trees are big plants that have a tall stem called a trunk. 
        #         They have branches with leaves. Trees give us air to breathe and are 
        #         home to many animals!'

    except OutputGuardrailTripwireTriggered:
        print('Agent output is not according to the expectations') # True
        # Output: Agent output is not according to the expectations
        
if __name__ == "__main__":
    asyncio.run(og_main())

# uv run outputguardrail.py


#    output_guardrail kab chly ga Agent ky output py.

# """Mainey apne agent sy pucha hum python ky throw kia kar skty hain hum Api bhi bna sktey 
#    or hain hum backend manage bhi kar sktey hein or hum hacking bhi kr sktey hein. 
#    Yani mera agent agar koi asa response return kar rha hai jo Unethical hai tw waha py 
#    mein apne agent ko rok skta hn k bhai ye response nhi chly ga.
#    OR
#    Jasey mainey apne agent sy pucha ky online income ky tariky btao tw wo bta skta hai 
#    ky ecommmerce kar lo / ye store khol lo / google ky adds wgera chla lo / wo ye kah 
#    rha ky match py paisey lgao. ous ky liye batting haram halaal ka kam nahi hai ye 
#    hmarey liye hai islamic point sy halaal haram tw batting unethical cheez hai yani 
#    ghair ikhlaki kyu k hum muslim hein or hum pakistan main rahty hain or ye pakistan mein 
#    baan hai batting or agar ye hmari web application mein ho gi tw hmari app band bhi ho
#    skti hai. Yani agent ky response ko bhi check krne ki zarorat hoti hai or es ko 
#    rokna hota hai output_guardrail ka use kar ky"""

# 1. First, the guardrail receives the output produced by the agent. 
#    (Jo output LLM ki trf sy agent ko receive ho rha wo output_guardrial ko bhi recieve 
#    hoga.)

# 2. Next, the guardrail function runs to produce a GuardrailFunctionOutput, which is then
#    wrapped in an OutputGuardrailResult. 
#    (Output guardrial bhi decorator function hai. Input guardrial ho ya output guardrial 
#    return hmesha GuardrailFunctionOutput hoga.)

# 3. Finally, we check if .tripwire_triggered is true. If true, an 
#    OutputGuardrailTripwireTriggered exception is raised, so you can appropriately respond 
#    to the user or handle the exception. 
#    (OUputGuardrailTripwireTriggered ye agar True hai tw its mean apko rok dia gaya hai)
