from agents import Agent, Runner
from main import config
from openai.types.responses import ResponseTextDeltaEvent
import asyncio


agent = Agent(
    name="Joker Agent",
    instructions="You are a helpful assistant."
)

async def run_main():
    result = Runner.run_streamed(
        agent,
        input="Please tell me 5 jokes.",
        run_config=config,
    )

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)
        # (for event) For Loop main for ky bad apna bnaya hua variable hota hai jis ko ap for loop k scope mein use karty ho
        # (in result.stream_events) yani target variable hota hai yani jis ka name apko ye event rakhna ho. yani result wala steam ko live dekhaye ga
        # Step-by-step chunks (like tokens or partial outputs).


if __name__ == "__main__": # Python main do trha ki file hoti hain aik wo file jo main entry point hoti hain jis ki zimadari ye hoti hai ky wo pure program ko run krey
    asyncio.run(run_main()) # ye function ko run krey ga.


# uv run runner.run_streamed.py

"""
# Stream yani Live streaming jasey Live Cricket match. 
# Yani jasey he token produce ho wasey he apky pass data ata rahy. Example jasey teacher 
# ki awaz.
# OR
# yani jasey he data/response generate ho wasey he hum tk pohnchta rahy LLM ki janib sy


Running agents
You can run agents via the Runner class. You have 3 options:

Runner.run_sync(), which is a sync method and just runs .run() under the hood.
Runner.run(), which runs async and returns a RunResult.
Runner.run_streamed(), which runs async and returns a RunResultStreaming. It calls the LLM in streaming mode, and streams those events to you as they are received.
"""

# Answer: 3
""""
Error mere pass a rha hai yaha wasey ye code sahi hai
"""