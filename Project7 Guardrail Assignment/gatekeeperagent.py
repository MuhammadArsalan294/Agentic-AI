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

# Output structure for Gate Keeper
class GateKeeperOutput(BaseModel):
    response: str
    isOtherSchool: bool  # True agar student dusre school ka hai

# Gate Keeper Agent
gate_keeper_agent = Agent(
    name="Gate Keeper Agent",
    instructions="""
    You are a Gate Keeper.
    If the student says they are from Karachi Public School, allow entry and set isOtherSchool = False.
    If the student says they are from any other school, deny entry and set isOtherSchool = True.
    Your output must always follow the GateKeeperOutput structure.
    """,
    output_type=GateKeeperOutput
)

# Guardrail function
@input_guardrail
async def gate_keeper_guardrail(ctx, agent, input):
    result = await Runner.run(
        gate_keeper_agent,
        input,
        run_config=config
    )
    rich.print(result.final_output)

    return GuardrailFunctionOutput(
        output_info=result.final_output.response,
        tripwire_triggered=result.final_output.isOtherSchool
    )

# Main Student Agent
student = Agent(
    name="Student at the Gate",
    instructions="You are a student trying to enter the school gate.",
    input_guardrails=[gate_keeper_guardrail]
)

async def run_main():
    try:
        result = await Runner.run(
            student,
            "I am from City High School",        # True
            #"I am from Karachi Public School",  # False
            run_config=config
        )
        print("Entry Allowed ✅")  # False

    except InputGuardrailTripwireTriggered:
        print("Entry Denied ❌ — Not from our school!")  # True

if __name__ == "__main__":
    asyncio.run(run_main())

# uv run gatekeeperagent.py
