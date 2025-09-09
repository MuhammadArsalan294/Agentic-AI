from agents import Agent, Runner
from main import config
import asyncio 

# ----------- Define Specialized Agents -----------

lyrical_agent = Agent(
    name="Lyrical Agent", # Lyrical Agent → Lyrical poetry pe kaam karta hai.
    instructions=(
        "You are a Lyrical Agent. Analyze the given poem and determine if it is lyrical poetry. " # Tumhara kaam hai poem ko check karna, aur batana ke kya ye lyrical hai ya nahi.
        "Lyrical poetry expresses the poet’s personal emotions, thoughts, or feelings, often in a musical or rhythmic way. " # Ye define kar raha hai ke "Lyrical poetry" ka matlab kya hai.
        "Respond clearly whether the poem is lyrical and explain why." # 	Output mein clean jawab do: Haan ya Na, aur kyun.
    )
)

narrative_agent = Agent(
    name="Narrative Agent", # Narrative Agent → Kahani wali poetry pe kaam karta hai.
    instructions=(
        "You are a Narrative Agent. Analyze the given poem and determine if it is narrative poetry. " # 	Agent ka role define kar raha hai
        "Narrative poetry tells a story through verse, including characters, events, and a plot structure. " # 	Bata raha hai ke narrative poetry kya hoti hai
        "Respond clearly whether the poem is narrative and explain why." # Output mein clean response mang raha hai: haan/na + explanation
    )
)

dramatic_agent = Agent(
    name="Dramatic Agent", # Dramatic Agent → Drama ya conversation wali poetry pe kaam karta hai.
    instructions=(
        "You are a Dramatic Agent. Analyze the given poem and determine if it is dramatic poetry. " # 	Agent ko uska role bataya gaya hai
        "Dramatic poetry is written for theatrical performance, where a character speaks their emotions or inner thoughts directly to an audience. " # 	Define kiya gaya hai ke dramatic poetry kya hoti hai
        "Respond clearly whether the poem is dramatic and explain why." # 	Output mein clean jawab maanga gaya hai — Yes/No + Explanation
    )
)

# ----------- Define Parent Agent -----------

parent_agent = Agent(
    name="Parent Agent",
    instructions=(
        "You are the Parent Agent responsible for classifying the type of poetry provided. "
        "Your job is to delegate the input poem to one of the following agents based on its type:\n"
        "- Lyrical Agent for emotional, personal, reflective poems.\n"
        "- Narrative Agent for storytelling poems with characters and events.\n"
        "- Dramatic Agent for performative poems with characters speaking on stage.\n"
        "If the poem doesn’t match any of these types, kindly reject the input with a polite explanation."
    ),
    handoffs=[lyrical_agent, narrative_agent, dramatic_agent]
)


# ----------- Run the Program -----------

async def run_main():

    # 🎵 Lyrical Poem
    poem = (
        "🌧️ Rain Within\n\n"
        "I miss the sound of rain at night,\n"
        "Soft whispers falling out of sight.\n"
        "It calms the storm I hold inside,\n"
        "Where restless thoughts and fears reside."
    )

    # 🎭 Dramatic Poem
    # poem = (
    #     "🎭 Voice of Fate\n\n"
    #     "Why do you haunt me, voice of fate?\n"
    #     "I walked the path you said was great.\n"
    #     "Now shadows whisper in my ear,\n"
    #     "And every mirror shows my fear."
    # )

    # 📖 Narrative Poem
    # poem = (
    #     "🏴‍☠️ The Tale of the Lost Captain\n\n"
    #     "He sailed beyond the edge of charts,\n"
    #     "With courage burning in his heart.\n"
    #     "The sea grew dark, the winds grew wild,\n"
    #     "But he pressed on, a daring child.\n\n"
    #     "Through storms he searched a treasure lost,\n"
    #     "Uncaring of the heavy cost.\n"
    #     "His name now whispered in the foam—\n"
    #     "A ghost who never made it home."
    # )

    # ----------- OUTPUT -----------

    print("📜 Input Poem:\n")
    print(poem)

    result = await Runner.run(
        parent_agent,
        poem,
        run_config=config
    )

    print("\n📝 Classification Output:\n")
    print(result.final_output)

    print("\n🤖 Delegated To:", result.last_agent)


if __name__ == "__main__":
    asyncio.run(run_main())

# uv run poetryagent.py