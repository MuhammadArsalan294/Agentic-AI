from main import config
from agents import Agent, Runner, ModelSettings, function_tool
import asyncio
import rich
import requests # For Fetching API


#################### Writer Agent OR Model Settings ####################

writer_agent = Agent(
    name = "Writer Agent",
    instructions=""" You are a helpful assistant that helps in writing blogs""",
    model_settings=ModelSettings(
        temperature=0.1,          # Low temperature (0.1) = Very focused, consistent answers
        #temperature=0.9,          # High temperature (0.9) = More creative, varied responses

        tool_choice="auto",       # Agent can decide when to use tools (default) # ye by default auto hoti hai LLM py chor dety hain hum tool call krey yya nhi
        #tool_choice="required",   # Agent MUST use a tool (even if not needed) # ye required hogi tw LLM tool call lazmi krey ga
        #tool_choice="none",       # Agent CANNOT use tools (chat only) # ye none hogi tw LLM tool call nhi krey ga
    )
)

async def main():
    result = await Runner.run(
        writer_agent,
        "Describe blood pressure",
        run_config=config,
    )
    rich.print(result.final_output)
    

if __name__ == "__main__":
    asyncio.run(main())


# uv run agentmodelsetting.py

"""
# ModelSetting sy LLM ko control karty hain /  ModelSetting sy apni application ky mind ko control kr rhy. ModelSetting es liye karna zarori hai 
# kyu ky hum har cheez LLM ky bharose nhi chor sktey.

# temperature: creativity and focused ko define krey ga. Ye 0.1 sy start hoga or 1.0 py khtm hoga yani ye float mein hogi

# 1.Temperature
    #model_settings=ModelSettings(temperature=0.1), # Low temperature (0.1) = Very focused, consistent answers 
    # Example: Agar aap equation solve karne ko kaho, toh ye sirf correct step-by-step calculation karega.

    #model_settings=ModelSettings(temperature=0.9), # High temperature (0.9) = More creative, varied responses 
    # Example: Agar aap story likhne ko kaho, toh ye har baar alag style aur unexpected twists ke sath likhega

# 2.Tool Choice

    #model_settings=ModelSettings(tool_choice="auto"), # Agent can decide when to use tools (default) 
    # agent_auto tools ko apni marzi se use karega.Agar question tools ke bina answer ho jata hai, toh direct jawab dega.Agar question me 
    # calculation ya weather ka kaam ho, toh tool call karega.Default behavior auto hai.

    #model_settings=ModelSettings(tool_choice="required"), # Agent MUST use a tool (even if not needed) 
    # agent_required ko hamesha tool use karna hi hoga.Even agar simple sawaal ho jaise "What is 2+2?", tab bhi wo calculator tool use karega.
    # Matlab direct jawab dena allowed nahi hai.

    #model_settings=ModelSettings(tool_choice="none"), # Agent CANNOT use tools (chat only) 
    # agent_no_tools ko tools ki access hi nahi hai.Ye sirf apne trained knowledge aur reasoning se jawab dega.Agar aap poochho "Weather in Lahore?", 
    # toh ye guess karega ya apna knowledge use karega, tool call nahi karega.

"""