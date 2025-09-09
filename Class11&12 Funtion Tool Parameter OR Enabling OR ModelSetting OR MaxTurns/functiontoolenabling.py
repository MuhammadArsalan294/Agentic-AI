from main import config
from agents import Agent, Runner, function_tool
import asyncio
import rich
import requests # For Fetching API

#################### Conditional Tool Enabling OR Function Tool Enabling  ####################


#def is_Admin():
#    return True # False

# First Example for is_Admin group
#def is_Admin():
#    admin_name = "Ali"
#    admins = ["Ali", "Ameen"]
#    if "Ali" in admins or "Ameen" in admins:
#       return True
#    else:
#        return False

# Second Example for is_Admin group
#def is_Admin():
#    admin_name = "Ali"
#    if admin_name == "Ali": # admin ka name ali tw True return kaaro warna False return kro 
#        return True
#    return False

# OR
    
def is_Admin():
    admin_name = "Ali"
    if admin_name == "Ali":
        return True
    else:
        return False


# First Example for is_Admin group by a dynamic function
@function_tool(name_override="Adding_Member_to_Whatsapp_group",
               description_override="Add a member to the whatsapp group only by the Admins",
               #is_enabled=True, # False
               is_enabled=is_Admin, # ye True or False bhi pass kr skty or Function name bhi
               )
def add_members():
    """
    This function Return the added member to the group 
    """
    members = []
    members.append("Ali")
    return "Member has been added to the group"


#################### Whatsapp Agent ####################

whatsapp_agent = Agent(
    name = "Whatsapp Agent",
    instructions=""" You are a admin of a whatsapp group your duty is to add members to the group""",
    tools=[add_members]
)

async def main():
    result = await Runner.run(
        whatsapp_agent,
        "Add Ali whatsapp group",
        run_config=config,
    )
    rich.print(result.new_items) # new_items es sy handsoff, tool calling or har cheez hmein jason form mein mil jati hai
    rich.print(result.final_output) # final_output es sy answer string mein aye ga


if __name__ == "__main__":
    asyncio.run(main())


# uv run functiontoolenabling.py


"""
Conditional tool enabling

# kia tool LLM ky liye enable hona chahiye ya nhi / wo tool jo LLM ko enable ya disable karna ho os ko khty Conditional tool enabling.
# Example mera whatsapp group hai sirf admin he os chez ko access kr skey/ Agar mere pass whatsapp group ka aik tool hai members ko add 
# krne ky liye tw wo sirf admin ky liye enable hoga or baki members ky liye disable hoga.

# is_enable kia krta hai hmarey tool ko enable krta hai ya disable. kis trha krey ga enable ya disable context, user preferences sy.
# is_enabled hmesha aik Boolean return krey ga True/False.
# is_enable by default True he hota hai.
# is_enabled=True hai tw mera tool enable hoga or wo mere LLM ko visible hoga.
# is_enabled=False hai tw mera tool disable hoga or wo mere LLM ko visible nhi hoga.

# is_enabled=True by default True
# if is_enabled=True iT will be visible to the LLM
# if is_enabled=False  iT will not be visible to the LLM

"""

"""
Conditional tool enabling

You can conditionally enable or disable agent tools at runtime using the is_enabled parameter. This allows you to dynamically filter 
which tools are available to the LLM based on context, user preferences, or runtime conditions.

"""   