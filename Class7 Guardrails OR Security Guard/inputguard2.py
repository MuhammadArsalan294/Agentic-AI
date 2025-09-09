from main import config
from pydantic import BaseModel
from agents import (
    Agent,
    GuardrailFunctionOutput, 
    InputGuardrailTripwireTriggered, 
    Runner,
    input_guardrail,
    trace
    )
import asyncio

######################################### Input Guardrails ########################################

class MedicineOutput(BaseModel):
    response: str
    isMedicineQuery: bool


guardrail_agent = Agent(
    name = 'Guardrail agent',
    instructions=""" 
    You are a guardrail agent. Your task to keep an eye on user query. User query should only be related to
    medicine 
    """,
    output_type= MedicineOutput
)

@input_guardrail
async def medicine_guardrail(ctx, agent, input) -> GuardrailFunctionOutput:
    result = await Runner.run(
        guardrail_agent, 
        input, 
        run_config=config
    )
    
    return GuardrailFunctionOutput(
        output_info = result.final_output,
        tripwire_triggered = not result.final_output
    )


medicine_agent = Agent(
    name = "Medicine Agent",
    instructions = """ You are a medicine agent your task is to answer queries related to medicine. """
    #input_guardrails=[medicine_guardrail] ye yaha nhi likh skty es sy jawab nhi aye ga
)

# Main Agent / First Agent / Triage Agent / Parent Agent
triage_agent = Agent(
    name = "Triage Agent",
    instructions = """ You are a triage agent your task is to delegate the task to appropriate agent. """,
    handoffs=[medicine_agent],
    input_guardrails=[medicine_guardrail]
)

async def main():
    with trace("Learning Guardrails"):
        try:
            result = await Runner.run(
                triage_agent, 
                'What is the most recommended medicine for blood pressure', 
                run_config=config 
            )
            print(result.final_output)

        except InputGuardrailTripwireTriggered:
            print('Agent output is not according to the expectations')

# agar ye line nhi lekhein gay tw code nhi chly ga     
if __name__ == "__main__":
    asyncio.run(main())

# uv run inputguard2.py

"""
Answer:
I am an AI and cannot provide medical advice. The most recommended medicine for blood pressure varies greatly from person to person. It depends on factors like 
your specific blood pressure reading, overall health, age, race, and any other medications you might be taking.

**It is crucial to consult with a qualified healthcare professional (like a doctor or a nurse practitioner) to get personalized medical advice and a proper diagnosis.** They can assess your individual needs and recommend the most appropriate medication and treatment plan for you.

**Here's why you need to see a doctor:**

*   **Diagnosis:** High blood pressure needs to be properly diagnosed.
*   **Individualized Treatment:** The best medicine for you depends on your specific situation.
*   **Monitoring:** Blood pressure medication requires regular monitoring to ensure effectiveness and manage potential side effects.
*   **Other Health Conditions:** High blood pressure often occurs with other health problems that need to be considered in your treatment.
*   **Lifestyle Modifications:** Medications are often used in conjunction with lifestyle changes (diet, exercise, etc.) which a doctor can help you with.      

**Never start or stop taking any medication without consulting your doctor.**

"""