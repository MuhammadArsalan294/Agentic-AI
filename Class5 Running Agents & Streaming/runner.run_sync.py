from agents import Agent, Runner
from main import config

def run_main():

    agent = Agent(
       name="Agent",
       instructions="You are a helpful assistant.",  # system prompt
    )
    
    result = Runner.run_sync(
       agent,
       "Hello, how are you?",  # user input
       run_config=config,
    )
    
    print(result.final_output)
    
if __name__ == "__main__": # Python main do trha ki file hoti hain aik wo file jo main entry point hoti hain jis ki zimadari ye hoti hai ky wo pure program ko run krey
    run_main()             # ye function ko run krey ga.

# uv run runner.run_sync.py

# jab tak phla kam nhi hota dusra nhi krey ga line by line chly ga 
# Jab tak response nahi a rha apko wait karna hoga. Yani jab tak response nahi a rha ap block hein. Example Form fill karty waqt.
# Jasey ky 1 folder hai 10 file hain Agent ka kam hai aik aik kar ky file ko read krey or phir database main bhejy jab tak ye 3 step complete naw ho agaye naw jaye. Example translator agent phle English main phir urdu mein phir arbi mein translate karna yani Step Step by step ya line by line
# OR
# Ye line by line kam karta hai. Jab tak 1 ka result nhi aye ga dusrey py nhi jaye ga yani wait krey ga 5 second ya kuch mints.
 
