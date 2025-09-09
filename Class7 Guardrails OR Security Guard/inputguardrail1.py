from main import config
from pydantic import BaseModel # ye library hai pydantic. BaseModel class ka name hai
from agents import (
    Agent,
    Runner, 
    input_guardrail, # ye Agent ki class sy import hua hai ye function hai ye hum ny decorator function mein use kia hai
    GuardrailFunctionOutput, # ye aik class hai
    InputGuardrailTripwireTriggered,
) 
import asyncio
import rich # uv add rich   run this commmand line


class PassengerOutput(BaseModel): # jab bhi child class ky round bracket main kisi dusri class ka name ho wo concept inheritance khlata hai or Class ky name ka phla word hmesha bara aye ga yani Capital 
    response: str  # ye keys define ki hai dono str OR bool / by default hmein string main answer milta hai
    isWeightExceed: bool


airport_security_guard = Agent(
    name="Airport Security Guard",
    instructions="""
    Your task is to check the passenger luggage.
    If passengers luggage is more then 25KGs, gracefully stop them.
    """,
    output_type= PassengerOutput #  output_type ka ye mtlb hai main apne data ko bana raha hon structure/dictionary/object.PassengerOutput ye upper hai class ka name 
)

@input_guardrail # jasey function tool ka decorator hota hai asey he input guardrial ka bhi decorator hota hai
async def security_guardrial(ctx, agent, input):  # ye same rahy ga name hmesha parameter ky andr
    result = await Runner.run(
        airport_security_guard,
        input,  # Your Input or your guardrial both receive the same input
        run_config=config
    )
    rich.print(result.final_output) # ab tak hmein string mein answer mil raha tha final_output py but yaha aik structure print ho raha hai Yani dictionary/object mein answer a raha hai

    return GuardrailFunctionOutput( # ye aik class hai
        output_info=result.final_output.response, # final_output by default string mein print hoti hai.  response ye upper sy likha hai
        tripwire_triggered=result.final_output.isWeightExceed # tripwire_triggered=True/False ye check krne k liye likhi thi  #  isWeightExceed: bool ye upper sy likha hai # ye hmesha BOOLEAN True/False return krey gi agar ye True hua its mean apki execution ruk jaye gi kyu ky apne misuse kia Or agar False hai tw everything is okk yani miduse nhi ho raha 
    )


# Main Agent
passenger = Agent(
    name="Passenger",
    instructions="Your are a passenger agent.",
    input_guardrails=[security_guardrial]  # input guardrial mein pass hoga function ka name
)

async def run_main():
    try:  # means janey do / chlny do
        result = await Runner.run(
            passenger,
            #"My luggage weight is 50Kgs ", # output py True aye ga   # Your Input or your guardrial both receive the same input
            "My luggage weight is 20Kgs ", # output py False aye ga  # Your Input or your guardrial both receive the same input
            run_config=config
        )
        print("Passenger is onbaord") # agartripwire_triggered=False hui tw ye chly ga / Ye agar False hai tw its means mere agent sy wo he kam karwaya ja rha hai jis ky liye wo bana hai / yani agent ka misuse nhi hua

    except InputGuardrailTripwireTriggered: # agar tripwire_triggered=True hui tw ye class chly ga / Ye agar True hai tw its means mere input guardrial ny mere agent ko miss use hone sy bacha lia hai / yani agent ka misuse hua
        print("Passenger cannot Check-In") 

# Run the async function
if __name__ == "__main__":
    asyncio.run(run_main()) # ye main agent likha hai ye sari file ko exeecute kar rha hai

# uv run inputguardrail1.py


 
# OpenAI Agents SDK (Search on google) then 
# https://openai.github.io/openai-agents-python/
# Guardrails

"""
# Guardrails do tarha ky hoty hain  input_guardrail OR output_guardrails.
# input_guardrail user ky input py chlty hein / user sy atey hein 
# Agent hmara LLM sy bat karta hai LLM hmara million and billion parameters of data sy train hai.

# Agar aik writer agent jo story likhta hai. Agar main apne writer agent sy asa kam karwaon 
# jis sy ous ka lena dena he nhi hai jasey hum ny puch lia ky python main dictionary kia hoti 
# hai writer agent ka kam hai sirf chezon ko likhna story/email etc likhna tw yaha py aik
# concept ata hai. Yani agent bana kis kam k liye hai or mein koi or kam karwa raha hon ous
# sy. Input guardrial ka ye he mtlb hai agent jis kam k liye bna hai os sy wo he kam krwaya 
# jaye agar aik writer agent hai tw wo sirf writing krey ga chahy wo essay likhy ya email/poem likhy.
 
# Input means jo user ki trf sy ata hai OR Guardrail ka mtlb hota hai security guard yani mere input ky
# upper aik security guard lga dia jaye ta ky mera agent jis kam k liye bana hai wo wo he kam krey koi
# or dusra kam nahi krey.
# OR
# Input guardrail m kia hota hai mean input guardrail user k input ko validate karta hai ta ky wo mere agent 
# sy wo he input pohchy jis k liye wo bana hai ous ky liye he use ho .
    
# Abhi hum gemini Api Key use kar rhy hein jo ky free main hai lekin real mein hum paid Api use krein gay
# jis k paisey cut hon gay jbhi hum input guardrial ka use kr rhy taky agent jis kam k liye bana hai ous
# sy wo he kam pucha jaye.

# Phle hmarey user ka input ata tha phir agent ky pass jata tha chahy hum jo bhi input dein.
# Ab user ky input mein or agent ky center m aik security guard hoga / user ky bad agent sy phle aik bech mein 
# security guard hoga jo hmarey input ko validate krey ga.
# OR
# Jasey hum shopping ky liye jaty hain waha jo scanner ya security guard hai bech mein. 
# Yani bech mein security guard hai hmari checking hogi yani hum ko validate kia ja raha hai.
# One more example airport sy bahir jana.

# Answer ye hum phle logs phir trace mein ja kar check kar skty hain 
# Phle passenger chla phir security guardrial chala tw jo security guardrail function hai wo itself apne 
# pass aik agent hai jis ka name hai airportSecurityGuard.
"""

"""
# 1.First, the guardrail receives the same input passed to the agent. 
#   (Yani Your guardrial or your input  both receive the same input.)

# 2.Next, the guardrail function runs to produce a GuardrailFunctionOutput, which is then wrapped in an InputGuardrailResult. 
#   (InputGuardrail aik decorator hai.Guardrail function chly ga tw wo hmesha return krey ga GuardrailFunctionOutput.)

# 3.Finally, we check if .tripwire_triggered is true. If true, an InputGuardrailTripwireTriggered exception is raised, 
#   so you can appropriately respond to the user or handle the exception.
#   (tripwire_triggered yani airport gaye koi asa saman nikal aya  jasey weapon nikl aya or hmein rok dia gaya 
#   bech main tw ye hota hai InputGuardrailTripwireTriggered.
#   InputGuardrailTripwireTriggered exceptin is raised means ky paper dety waqt sir ny cheating karty waqt hmein 
#   rok dia its means os ny apna kam kar dia.
#   InputGuardrailTripwireTriggered ye agar true hai tw its mean apko rok dia gaya hai.)

#   Note
#   Input guardrails are intended to run on user input, so an agent's guardrails only run if the agent is the first agent. 
#   You might wonder, why is the guardrails property on the agent instead of passed to Runner.run? It's because guardrails
#   tend to be related to the actual Agent - you'd run different guardrails for different agents, so colocating the code is
#   useful for readability.
#   (Input guardrail hmesha user ky input py chlta hai, or input guardrail hmesha first agent yani main/parent agent py chlta hai 
#   Yani first agent wo hota hai jo user ki query ko face karey)
"""


"""
PassengerOutput(response='Your luggage is within the weight limit. Have a nice flight!', isWeightExceed=False)
Passenger is onbaord
"""


