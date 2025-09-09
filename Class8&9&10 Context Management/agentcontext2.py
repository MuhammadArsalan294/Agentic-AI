from main import config
from pydantic import BaseModel
from agents import( 
    Agent, 
    Runner,
    RunContextWrapper,  
    function_tool, 
    trace
)
import asyncio
import rich

from dotenv import load_dotenv
load_dotenv()

# ------------------ Example of Local Context ------------------ #

#class CartItems(BaseModel):
#    product: list
#    user_id: int
#    brand: str
#    total_amount: int

#cart = CartItems(
#    product=["Mobile", "Laptop"], 
#    user_id="923001234567", 
#    brand="apple", 
#    total_amount=342398
#)

#async def MyPersonalFunction(wrapper: RunContextWrapper[CartItems]):
#    return wrapper

#@function_tool # normal function asynchronous/synchronous bhi ho skta or function tool bhi ho skta hai jis sy mera data LLM tak pohnchy ga
#def products_info(wrapper: RunContextWrapper[CartItems]):
#    print('Checking Context', wrapper)
#    return f'{wrapper.context}'

# ------------------ Example of Agent/LLM Context ------------------ #

class Person(BaseModel):
    name: str
    user_level: str

# instance/object 
personOne = Person(
    name = "Ali",
    user_level = "Junior" # "PHD"
)


def my_dynamic_instructions(ctx: RunContextWrapper[Person], agent: Agent): #ye function do parameter lazmi lein gay or return karna bhi lazmi ho ga # ctx parameter hai or RunContextWrapper eik class hai es class ki bhi aik class/type hai Person or [Person] es ko generics khty hain generic ka mtlb hai aik asi chez jo register nhi wo kisi ky sath bhi adjust ho jaye os ko koi bhi use kar ly jasey water generic hai Or Agent agent ky module sy import kar rhy hain. RunContextWrapper Junior or PHD ko mila raha hai instruction sy OR Dynamic instruction jo hai wo local context sy connect ho kar jata hai
    # yaha wo system prompt/input aye ga jo instruction main likhty thy or aaj tak hum instruction string main dety thy but aaj function mein di hai dynamic instructions OR situation/context awareness  dynamic instruction sy hoti hai or yaha ho rhi hai
    if ctx.context.user_level == 'junior' or ctx.context.user_level == 'mid_level': # ctx variable sy a raha or context RunContextWrapper sy a rha or user_level Person ki class sy a rha / and operator jitni conditon sari true hon / or mein aik bhi condition true hui answer true hoga
        return """
        Keep your answers simple and easy to understand.
        """
    elif ctx.context.user_level == "PHD":
        return """ 
        Keep you vocabulary advanced and very hard like your are talking to a PHD level peron 
        """

personal_agent = Agent(
    name = "Agent",
    instructions= my_dynamic_instructions,# ye upper sy likha #dynammic instructions ap ous waqt krty ho jab apko agent ky instruction ka parameter badlna ho ta ky ap apne agent ko situation or context ki awareness dy skko  
)

async def main():
    with trace("Learn Dynamic Instructions"):
        result = await Runner.run(
            personal_agent, 
            'What is light?', # User prompt/input
            run_config=config,
            context = personOne #Local context
            )
        rich.print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())

# uv run agentcontext2.py


"""
Answer:
Light is a fascinating and complex phenomenon that can be described in a few different ways, depending on the context.  Here's a breakdown of the key        
aspects:

**1. As an Electromagnetic Wave:**

*   **Nature:** Light is a form of electromagnetic radiation. This means it's a wave that is created by the interaction of electric and magnetic fields.     
These fields oscillate perpendicular to each other and to the direction the wave is traveling.
*   **Spectrum:** The electromagnetic spectrum encompasses a broad range of wavelengths, from radio waves to gamma rays.  "Light," in the narrowest sense,   
refers to the portion of the electromagnetic spectrum that is visible to the human eye.
*   **Wavelength and Frequency:**  Electromagnetic waves are characterized by their wavelength (the distance between two successive crests or troughs) and   
frequency (the number of waves that pass a point in a given time). Wavelength and frequency are inversely proportional:  longer wavelengths have lower       
frequencies, and shorter wavelengths have higher frequencies.
*   **Color:** The different wavelengths of visible light correspond to different colors. Red light has the longest wavelength, while violet light has the   
shortest.

**2. As a Stream of Particles (Photons):**

*   **Quantum Mechanics:** In quantum mechanics, light is also described as consisting of discrete packets of energy called photons.
*   **Energy:**  The energy of a photon is directly proportional to its frequency (and inversely proportional to its wavelength).  Higher frequency (shorter 
wavelength) light, like ultraviolet or X-rays, has higher energy photons.
*   **Wave-Particle Duality:** Light exhibits *wave-particle duality*.  This means that it can behave as both a wave and a particle, depending on how it is  
observed and measured.  Some experiments demonstrate wave-like properties (like diffraction and interference), while others demonstrate particle-like        
properties (like the photoelectric effect).

**3. Key Properties of Light:**

*   **Speed:** Light travels at an incredibly fast speed, often denoted as 'c', which is approximately 299,792,458 meters per second (in a vacuum).  This is 
the fastest speed possible in the universe.
*   **Reflection:** Light bounces off surfaces. The angle of incidence (the angle at which light strikes the surface) is equal to the angle of reflection.   
*   **Refraction:** Light bends when it passes from one medium to another (e.g., from air to water).  This bending is due to the change in the speed of lightas it enters the new medium.
*   **Diffraction:** Light bends around obstacles or through narrow openings.  This is more pronounced when the size of the obstacle or opening is comparableto the wavelength of the light.
*   **Interference:**  When two or more light waves overlap, they can interfere with each other, either constructively (resulting in a brighter light) or    
destructively (resulting in a dimmer light or darkness).
*   **Polarization:** Light waves can be polarized, meaning that the electric field oscillates in a specific direction.

**In Summary:**

Light is a form of electromagnetic radiation that exhibits wave-particle duality. It travels at the speed of light and possesses properties such as
reflection, refraction, diffraction, interference, and polarization. It can be described as both a wave, characterized by wavelength and frequency, and as a 
stream of particles called photons, each carrying a specific amount of energy.

The exact "nature" of light is still a topic of philosophical and scientific discussion, but the models we have are incredibly successful at describing and  
predicting its behavior.
"""
