from agents import Agent, Runner
from main import config


agent = Agent(
    name="Agent",
    instructions="You are a helpful assistant.",  # system prompt/input
)

def run_main(): 
    result = Runner.run_sync(
       agent,
       "Hello, how are you?",  # user prompt/input
       run_config=config,
    )
    
    print(result.final_output)
    
if __name__ == "__main__": # Python main do trha ki file hoti hain aik wo file jo main entry point hoti hain jis ki zimadari ye hoti hai ky wo pure program ko run krey
    run_main()             # ye function ko run krey ga.

# uv run runner.run_sync.py

"""
# jab tak phla kam nhi hota dusra nhi krey ga line by line chly ga 
# Jab tak response nahi a rha apko wait karna hoga. Yani jab tak response nahi a rha ap 
# block hein. Example Form fill karty waqt.
# Jasey ky 1 folder hai 10 file hain Agent ka kam hai aik aik kar ky file ko read krey 
# or phir database main bhejy jab tak ye 3 step complete naw ho agaye naw jaye. 
# Example translator agent phle English main phir urdu mein phir arbi mein translate 
# karna yani Step Step by step ya line by line
# OR
# Ye line by line kam karta hai. Jab tak 1 ka result nhi aye ga dusrey py nhi jaye ga 
# yani wait krey ga 5 second ya kuch mints.

Running agents
You can run agents via the Runner class. You have 3 options:

Runner.run_sync(), which is a sync method and just runs .run() under the hood.
Runner.run(), which runs async and returns a RunResult.
Runner.run_streamed(), which runs async and returns a RunResultStreaming. It calls the LLM in streaming mode, and streams those events to you as they are received.
""" 

# Answer: 1
"""
I am doing well, thank you for asking! As a large language model, I don't experience feelings 
or emotions like humans do, but I'm functioning optimally and ready to assist you. How can I help you today?
"""