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

class Traveler(BaseModel):
    name: str
    trip_type: str           # "adventure", "cultural", "business"
    traveler_profile: str    # "solo", "family", "executive", "medical_student", "doctor"

# Example instance
userOne = Traveler(
    name = "Sara",
    trip_type = "adventure",
    traveler_profile = "solo"
)

# ------------------ Dynamic Instructions ------------------ #

def travel_dynamic_instructions(ctx: RunContextWrapper[Traveler], agent: Agent):
    trip = ctx.context.trip_type.lower()
    profile = ctx.context.traveler_profile.lower()

    # Adventure + Solo
    if trip == "adventure" and profile == "solo":
        return """
        Recommend thrilling outdoor activities such as hiking, rafting, or safaris. 
        Provide safety tips specifically for solo travelers. 
        Suggest social hostels and group tours to encourage meeting new people. 
        Keep the tone exciting and reassuring.
        """

    # Cultural + Family
    elif trip == "cultural" and profile == "family":
        return """
        Focus on educational attractions, cultural landmarks, and interactive museums. 
        Highlight family-friendly accommodations and kid-safe dining options. 
        Suggest activities that are both fun and educational for children. 
        Keep the tone warm and family-oriented.
        """

    # Business + Executive
    elif trip == "business" and profile == "executive":
        return """
        Emphasize convenience and efficiency. 
        Recommend hotels close to airports and business districts. 
        Highlight business centers, reliable Wi-Fi, premium lounges, and fast check-in options. 
        Keep the tone concise and professional.
        """

    # Medical Student
    elif profile == "medical_student":
        return """
        Recommend affordable but educational trips. 
        Suggest attending medical conferences, workshops, and cultural exchanges. 
        Include budget accommodations and networking opportunities for learning. 
        Keep the tone encouraging and academic.
        """

    # Doctor
    elif profile == "doctor":
        return """
        Suggest wellness and relaxation-focused travel plans. 
        Recommend spa resorts, retreats, and medical conferences if relevant. 
        Highlight opportunities for professional networking and rejuvenation. 
        Keep the tone respectful and professional.
        """

    # Default fallback
    else:
        return """
        Provide helpful, tailored travel advice depending on trip type and traveler profile. 
        Keep the tone polite, clear, and adaptive.
        """

# ------------------ Agent ------------------ #

travel_agent = Agent(
    name = "TravelPlanningAgent",
    instructions= travel_dynamic_instructions,
)

# ------------------ Runner ------------------ #

async def main():
    with trace("Travel Dynamic Instructions"):
        result = await Runner.run(
            travel_agent, 
            "Can you suggest a travel plan for me?",  # user input
            run_config=config,
            context = userOne  # Local context
        )
        rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

# uv run agentcontext3.py