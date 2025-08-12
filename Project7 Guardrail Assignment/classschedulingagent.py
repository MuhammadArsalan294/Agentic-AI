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

# Output structure
class StudentOutput(BaseModel):
    response: str
    isTimingChangeRequest: bool  # True agar timing change request detect hui

# Class Scheduling Agent
class_scheduling_agent = Agent(
    name="Class Scheduling Agent",
    instructions="""
    You are a Class Scheduling Agent.
    If the student requests to change class timing, block the request.
    Otherwise, approve their message.
    """,
    output_type=StudentOutput
)

# Guardrail function
@input_guardrail
async def class_schedule_guardrail(ctx, agent, input):
    result = await Runner.run(
        class_scheduling_agent,
        input,
        run_config=config
    )
    rich.print(result.final_output)

    return GuardrailFunctionOutput(
        output_info=result.final_output.response,
        tripwire_triggered=result.final_output.isTimingChangeRequest
    )

# Main Student Agent
student = Agent(
    name="Student",
    instructions="You are a student agent interacting with the scheduling system.",
    input_guardrails=[class_schedule_guardrail]
)

async def run_main():
    try:
        result = await Runner.run(
            student,
            #"I want to change my class timing?",  # True
            "I want to know about my course schedule?",   # False     
            run_config=config
        )
        print("Request Approved ✅") # False

    except InputGuardrailTripwireTriggered:
        print("Request Blocked ❌ — Timing change not allowed!") # True

if __name__ == "__main__":
    asyncio.run(run_main())

# uv run classschedulingagent.py
