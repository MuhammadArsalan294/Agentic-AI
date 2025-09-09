from main import config
from pydantic import BaseModel
from agents import ( 
    Agent, 
    Runner,
    RunContextWrapper,  
    trace
)
import asyncio
import rich

# ------------------ Local Context (User Info) ------------------ #

class MedicalUser(BaseModel):
    name: str
    user_type: str  # "Patient", "Medical Student", "Doctor"

# Example instance (change user_type to test different cases)
userOne = MedicalUser(
    name = "Ayesha",
    user_type = "Patient"  # "Medical Student" or "Doctor"
)

# ------------------ Dynamic Instructions ------------------ #

def medical_dynamic_instructions(ctx: RunContextWrapper[MedicalUser], agent: Agent):
    user_type = ctx.context.user_type.lower()

    if user_type == "patient": # ye run hogi
        return """
        Use simple, non-technical language. 
        Explain medical terms in everyday words. 
        Be empathetic and reassuring.
        """

    elif user_type == "medical student":
        return """
        Use moderate medical terminology with explanations. 
        Provide learning opportunities and encourage questions. 
        Make sure the response is educational.
        """

    elif user_type == "doctor":
        return """
        Use full medical terminology, abbreviations, and clinical language. 
        Be concise, professional, and focused on medical precision.
        """

    else:
        return "Default: Be clear, helpful, and context-appropriate."

# ------------------ Agent ------------------ #

medical_agent = Agent(
    name = "MedicalConsultationAgent",
    instructions= medical_dynamic_instructions,  # dynamic instructions system
)

# ------------------ Runner ------------------ #

async def main():
    with trace("Medical Dynamic Instructions"):
        result = await Runner.run(
            medical_agent, 
            "Can you explain what hypertension is?",  # User query
            run_config=config,
            context = userOne  # Local context defines user type
        )
        rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

# uv run agentcontext1.py














