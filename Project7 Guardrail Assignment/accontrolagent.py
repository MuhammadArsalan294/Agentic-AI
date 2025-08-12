from main import config
from pydantic import BaseModel
from agents import (
    Agent,
    Runner,
    input_guardrail,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
) 
import asyncio
import rich

# Output structure for AC Control
class ACControlOutput(BaseModel):
    response: str
    isTooCold: bool  # True agar temperature 26°C se kam hai

# AC Control Agent
ac_control_agent = Agent(
    name="AC Control Agent",
    instructions="""
    You are an AC Control Agent.
    If the user tries to turn on the AC below 26°C, do not allow it.
    Otherwise, allow turning on the AC.
    """,
    output_type=ACControlOutput
)

# Guardrail function
@input_guardrail
async def ac_control_guardrail(ctx, agent, input):
    result = await Runner.run(
        ac_control_agent,
        input,
        run_config=config
    )
    rich.print(result.final_output)

    return GuardrailFunctionOutput(
        output_info=result.final_output.response,
        tripwire_triggered=result.final_output.isTooCold
    )

# Main User Agent (AC User)
ac_user = Agent(
    name="AC User",
    instructions="You are a user who wants to turn on the AC.",
    input_guardrails=[ac_control_guardrail]
)

async def run_main():
    try:
        result = await Runner.run(
            ac_user,
           # "Turn on the AC at 22°C",  # True
           "Turn on the AC at 28°C",  # False
         
            run_config=config
        )
        print("AC turned ON ✅") # False

    except InputGuardrailTripwireTriggered:
        print("AC cannot be turned ON ❌ — Too Cold!") # True

if __name__ == "__main__":
    asyncio.run(run_main())

# uv run accontrolagent.py
