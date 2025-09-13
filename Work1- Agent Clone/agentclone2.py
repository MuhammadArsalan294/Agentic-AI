from main import config
from agents import Agent, ModelSettings, Runner


###############  Cloning with Different Settings ###############

# Base agent
base_agent = Agent(
    name="BaseAssistant",
    instructions="You are a helpful assistant.",
    model_settings=ModelSettings(temperature=0.7)
)


# Clone with different temperature
creative_agent = base_agent.clone(
    name="CreativeAssistant",
    instructions="You are a creative writing assistant.",
    model_settings=ModelSettings(temperature=0.9)  # Higher creativity
)


precise_agent = base_agent.clone(
    name="PreciseAssistant", 
    instructions="You are a precise, factual assistant.",
    model_settings=ModelSettings(temperature=0.1)  # Lower creativity
)


# Test creativity levels
query = "Describe a sunset."


result_creative = Runner.run_sync(
    creative_agent, 
    query,
    run_config=config # ye likhy bghr error a rha tha
)


result_precise = Runner.run_sync(
    precise_agent, 
    query,
    run_config=config
)


print("Creative:", result_creative.final_output)
print("Precise:", result_precise.final_output)

# uv run agentclone2.py

"""
Anser:

Creative: The sun, a molten coin in the sky, began its slow descent. It wasn't a sudden plunge, but a graceful yielding, a painter dipping their brush in hues of fire and spreading them across the canvas of the heavens.

First, the blue surrendered, fading into softer shades of lavender and rose. Then, a brazen orange erupted, licking the clouds like flames, transforming them into shimmering embers. Streaks of crimson bled into the horizon, painting the world in a passionate, fleeting blush.

The clouds, once cottony and white, became dramatic masterpieces: towering castles of gold, wispy brushstrokes of amethyst, and jagged peaks of burnished bronze. They caught the light, amplified it, and flung it back down to earth in a dazzling display.

As the sun dipped lower, the colors deepened and intensified. The air grew thick with a golden haze, softening the edges of the world, blurring the lines between reality and dream. Silhouettes of trees stood like silent sentinels, watching the fiery spectacle unfold.

Finally, with a final, breathtaking flourish, the sun slipped below the horizon. The fiery hues began to fade, replaced by softer shades of violet and indigo. The sky held its breath for a moment, a lingering echo of the vibrant show, before surrendering to the quiet embrace of twilight.

And as the first stars began to prick through the darkening sky, a sense of peace settled over the world, a promise of rest and renewal after the day's fiery farewell. The sunset was gone, but its memory lingered, a warm ember glowing in the heart of the night.

Precise: A sunset is the daily disappearance of the Sun below the horizon due to Earth's rotation. As the sun approaches the horizon, its light travels through 
a greater amount of atmosphere, reducing the intensity of direct sunlight and scattering away blue light. This leaves a higher proportion of other wavelengths, 
such as orange and red, which are visible to the human eye. The colors of a sunset vary depending on atmospheric conditions, including the presence of aerosols 
like dust, smoke, or pollutants. These particles can scatter light and create more vivid and prolonged sunsets. The process typically involves a transition from brighter yellows and oranges to deeper reds and purples as the sun descends further.

"""
