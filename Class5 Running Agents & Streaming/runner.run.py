from agents import Agent, Runner
from main import config
import asyncio # Import async ye module hai python main. Ye A syncronous kam karne mein help krta hai 

async def run_main():

    agent = Agent(
        name = "Agent",
        instructions = "You are a helpfull assistant.", # system prompt
    )

    result = await Runner.run(
        agent,
        "Hello, how are you?", # user input
        run_config = config,
    )

    print(result.final_output)

if __name__ == "__main__": # Python main do trha ki file hoti hain aik wo file jo main entry point hoti hain jis ki zimadari ye hoti hai ky wo pure program ko run krey
    asyncio.run(run_main()) # ye function ko run krey ga.

# uv run runner.run.py

# Phle kam ki waja sy dusra kam delay nhi krey ga phle dusra krey ga phir wait yani (5 second) bad phla kam krey ga
# ye kam ko block nhi krey ga / Jis ki execution block naw ho / User wait naw krey. Example Youtube 
# Asynchronous ky sath await lgy ga 

