from agents import Agent, Runner, ModelSettings
from main import config # import module ye main file sy import kia

# / Openai Agents SDK / uv add openai-agents 
agent = Agent(
    name = "General Agent",
    instructions = "You are a helpful assistant. Your task is to help the user with their queries",

    # 1. Temperature - The Creativity Knob
    #model_settings=ModelSettings(temperature=0.1), # Low temperature (0.1) = Very focused, consistent answers # Example: Agar aap equation solve karne ko kaho, toh ye sirf correct step-by-step calculation karega.
    #model_settings=ModelSettings(temperature=0.9), # High temperature (0.9) = More creative, varied responses # Example: Agar aap story likhne ko kaho, toh ye har baar alag style aur unexpected twists ke sath likhega

    # 3. Max Tokens - The Response Length Limit
    #model_settings=ModelSettings(max_tokens=100), # Short, concise responses  # agent_brief ke liye max_tokens=100 set hai.Matlab iska jawab sirf short aur concise hoga, unnecessary detail nahi dega.Useful jab quick answers chahiyein (FAQs, SMS-style reply).
    #model_settings=ModelSettings(max_tokens=1000), # Longer, detailed responses  # agent_detailed ke liye max_tokens=1000.Matlab iska jawab zyada detailed aur lamba ho sakta hai.Useful jab explanation, essay, ya in-depth reasoning chahiye ho.

    # Example 1: Math Tutor with Low Temperature
    #model_settings=ModelSettings(
    #    temperature=0.1,  # Very focused # responses consistent aur accurate rahenge.
    #    max_tokens=500    # Enough for detailed steps # kaafi lamba jawab aa sakta hai (detailed explanation ke liye).
    #),

    # Example 2: Creative Writer with High Temperature
    #model_settings=ModelSettings(
    #    temperature=0.8,  # Very creative # zyada creativity aur variation allow karta hai.
    #    max_tokens=300    # Short but creative # chhoti par expressive story generate karega.
    #)
)

result = Runner.run_sync( # Runner.run_sync yani 2+2=4 then *4 ye sequence sy chlta hai
    agent,
    'Who is the founder of Pakistan', # Historical Data
    #'What is the conversion rate of USD to PKR', # Real time data ye answer nhi dy ga sorry kr ly ga ya purana data dy ga  answer k liye humein tool calling ka use krna hoga
    #'Show me the top 10 student of class 10', # Personalised data ye answer nhi dy ga sorry kr ly ga ya purana data dy ga  answer k liye humein tool calling ka use krna hoga
    run_config=config
)

print(result.final_output)

# uv run toolnotusehistoricaldata.py

# API = Application Programming Interface

"""
# Types Of Data(LLM DataSet)
# 1.Non realtime data / Historical Data
#   Purani batein / jo phle sy data moujod ho
#   Exaample: Who is the founder of Pakistan

# 2.Realtime data / Current Data
#   Yani wo data jis mein aaj kal ki bat ho rahi ho
#   Example: Current Date, Currency Rate, Weather update

# 3.Personalised Data / Personal Data
#   Yani wo data jo apka personal ho
#   Example: Resume/CV, Company Data, Student Details

# LLM DataSet 
# LLM ky pass Real time data or Personalised data nhi hota es ky liye hum Tool Calling 
# ka use karty hain
"""

# Answer:
"""
Muhammad Ali Jinnah is generally considered the founder of Pakistan. He was the leader of the 
All-India Muslim League and led the movement for the creation of a separate nation for Muslims in British India.
"""