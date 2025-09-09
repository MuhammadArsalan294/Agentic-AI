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

# ------------------ Local Context ------------------ #

class AirlineUser(BaseModel):
    name: str
    seat_preference: str       # "window", "aisle", "middle", "any"
    travel_experience: str     # "first_time", "occasional", "frequent", "premium"

# Example instance
userOne = AirlineUser(
    name = "Ahmed",
    seat_preference = "window",
    travel_experience = "first_time"
)

# ------------------ Dynamic Instructions ------------------ #

def airline_dynamic_instructions(ctx: RunContextWrapper[AirlineUser], agent: Agent):
    seat = ctx.context.seat_preference.lower()
    exp = ctx.context.travel_experience.lower()

    # Window + First-time
    if seat == "window" and exp == "first_time": # and operator main aik bhi condition false hui tw answer false hoga yani sab condition true hon
        return """
        Highlight the benefits of a window seat, such as scenic views and personal space. 
        Be reassuring and empathetic to ease first-time traveler concerns. 
        Keep the explanation friendly and encouraging.
        """

    # Middle + Frequent
    elif seat == "middle" and exp == "frequent":
        return """
        Acknowledge the inconvenience of middle seats. 
        Suggest strategies (e.g., choosing exit rows, early check-in) and offer practical alternatives. 
        Keep the tone professional and efficient for frequent flyers.
        """

    # Any + Premium
    elif seat == "any" and exp == "premium":
        return """
        Emphasize luxury and comfort options, such as flatbeds, lounge access, and upgrades. 
        Highlight premium services like priority boarding and extra space. 
        Use polished, concierge-style language.
        """

    # Default fallback
    else:
        return """
        Provide general helpful guidance about seat selection. 
        Keep tone polite, clear, and context-aware.
        """

# ------------------ Agent ------------------ #

airline_agent = Agent(
    name = "AirlineSeatPreferenceAgent",
    instructions= airline_dynamic_instructions,
)

# ------------------ Runner ------------------ #

async def main():
    with trace("Airline Dynamic Instructions"):
        result = await Runner.run(
            airline_agent, 
            "Which seat would be best for me?",  # user input
            run_config=config,
            context = userOne  # Local context
        )
        rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

# uv run agentcontext2.py














