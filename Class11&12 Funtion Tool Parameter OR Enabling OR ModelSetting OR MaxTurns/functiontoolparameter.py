from main import config
from agents import Agent, Runner, function_tool
import asyncio
import rich
import requests # For Fetching API


#################### Function Tool ####################

@function_tool # Decorater Parent Funtion hai 
def get_current_location(): # Ye Child Funtion hai
    return "Governor House Karachi"

#@function_tool
#def get_current_location():
#    url = requests.get('my_google_maps_api') # get method yani api sy data lia or aik post method bhi hota hai
#    return url.json()                        # yaha json es liye likha jab hum server sy bat krty tw json format main krty hain 


#################### Function Tool Parameter(name, discription) And Doc String ####################


@function_tool(name_override="Get_Location", #  Decorater Parent Funtion hai. # by default get_current_location funtion ka name tha or  Get_Location new name rakh dia yani function ka name change kar dia or Get Location space ky sath nhi aye ga
               description_override="Get the current location of a user") # jasey fuction ka name change kar skty asey discription bhi dy skty hain discription by default empty thi hum ny yaha provide ki tw ab discription main ye show hogi discription 
def get_current_location() -> str: # Ye Child Funtion hai. # Ye by default function ka name hota hai. Return string kar rha jbhi str likha agr dictionnary return hoti tw dict likhty agr list return karta tw list agar number return krta tw int 
    # Doc String Means Documentation String. Doc String apke function ki documentation bnata hai / Doc String explain karta hai ky apky function main kia kia ho rha hai ya apka function kia kar rha hai
    """
    Return the current location
    """
    return "Governor House Karachi"


# Ye dono Addition function ka name same hai or hum decorator function sy parameter sy function ka name jbhi change karty hain ta ky confusion naw ho.
@function_tool
def Addition():
    return 10 * 7

@function_tool(name_override="Add_Number")
def Addition(num1, num2) -> int: # num1 first parameter hai
    """
    num1: int Takes the first number as an arguments

    Return the addition of two numbers
    """
    return 10 + 7

# Only Doc String Define
def book_a_cab(by, to, amount):
    """
    by: users current location
    to: users destination
    amount: int The amount to be charged for the ride

    Return the destination, current location and amount
    
    """
    return {by: "GH", to: "Home", amount: 500}


#################### Personal Agent ####################

personal_agent = Agent(
    name = "Agent",
    instructions = """
    You are a helpful assistant always call a tool to get the location.
    """, # multi line string
    tools = [get_current_location]
)


async def main():
    result = await Runner.run(
        personal_agent,
        "What is my current location",
        run_config=config,
    )
    rich.print(result.new_items) # new_items es sy handsoff, tool calling or har cheez hmein jason form mein mil jati hai
    rich.print(result.final_output) # final_output es sy answer string mein aye ga


if __name__ == "__main__":
    asyncio.run(main())


# uv run functiontoolparameter.py


"""
[
    ToolCallItem(
        agent=Agent(
            name='Agent',
            handoff_description=None,
            tools=[
                FunctionTool(
                    name='get_current_location', # yaha name change hoga
                    description='',              # yaha description a jaye gi
                    params_json_schema={
                        'properties': {},
                        'title': 'get_current_location_args',
                        'type': 'object',
                        'additionalProperties': False,
                        'required': []
                    },
                    on_invoke_tool=<function function_tool.<locals>._create_function_tool.<locals>._on_invoke_tool at 0x0000017547A2AAC0>,
                    strict_json_schema=True,
                    is_enabled=True
                )
            ],
            mcp_servers=[],
            mcp_config={},
            instructions='\n    You are a helpful assistant always call a tool to get the location\n    ',
            prompt=None,
            handoffs=[],
            model=None,
            model_settings=ModelSettings(
                temperature=None,
                top_p=None,
                frequency_penalty=None,
                presence_penalty=None,
                tool_choice=None,
                parallel_tool_calls=None,
                truncation=None,
                max_tokens=None,
                reasoning=None,
                verbosity=None,
                metadata=None,
                store=None,
                include_usage=None,
                response_include=None,
                top_logprobs=None,
                extra_query=None,
                extra_body=None,
                extra_headers=None,
                extra_args=None
            ),
            input_guardrails=[],
            output_guardrails=[],
            output_type=None,
            hooks=None,
            tool_use_behavior='run_llm_again',
            reset_tool_choice=True
        ),
        raw_item=ResponseFunctionToolCall(arguments='{}', call_id='', name='get_current_location', type='function_call', id='__fake_id__', status=None),        
        type='tool_call_item'
    ),
    ToolCallOutputItem(
        agent=Agent(
            name='Agent',
            handoff_description=None,
            tools=[
                FunctionTool(
                    name='get_current_location',
                    description='',
                    params_json_schema={
                        'properties': {},
                        'title': 'get_current_location_args',
                        'type': 'object',
                        'additionalProperties': False,
                        'required': []
                    },
                    on_invoke_tool=<function function_tool.<locals>._create_function_tool.<locals>._on_invoke_tool at 0x0000017547A2AAC0>,
                    strict_json_schema=True,
                    is_enabled=True
                )
            ],
            mcp_servers=[],
            mcp_config={},
            instructions='\n    You are a helpful assistant always call a tool to get the location\n    ',
            prompt=None,
            handoffs=[],
            model=None,
            model_settings=ModelSettings(
                temperature=None,
                top_p=None,
                frequency_penalty=None,
                presence_penalty=None,
                tool_choice=None,
                parallel_tool_calls=None,
                truncation=None,
                max_tokens=None,
                reasoning=None,
                verbosity=None,
                metadata=None,
                store=None,
                include_usage=None,
                response_include=None,
                top_logprobs=None,
                extra_query=None,
                extra_body=None,
                extra_headers=None,
                extra_args=None
            ),
            input_guardrails=[],
            output_guardrails=[],
            output_type=None,
            hooks=None,
            tool_use_behavior='run_llm_again',
            reset_tool_choice=True
        ),
        raw_item={'call_id': '', 'output': 'Governor House Karachi', 'type': 'function_call_output'},
        output='Governor House Karachi',
        type='tool_call_output_item'
    ),
    MessageOutputItem(
        agent=Agent(
            name='Agent',
            handoff_description=None,
            tools=[
                FunctionTool(
                    name='get_current_location',
                    description='',
                    params_json_schema={
                        'properties': {},
                        'title': 'get_current_location_args',
                        'type': 'object',
                        'additionalProperties': False,
                        'required': []
                    },
                    on_invoke_tool=<function function_tool.<locals>._create_function_tool.<locals>._on_invoke_tool at 0x0000017547A2AAC0>,
                    strict_json_schema=True,
                    is_enabled=True
                )
            ],
            mcp_servers=[],
            mcp_config={},
            instructions='\n    You are a helpful assistant always call a tool to get the location\n    ',
            prompt=None,
            handoffs=[],
            model=None,
            model_settings=ModelSettings(
                temperature=None,
                top_p=None,
                frequency_penalty=None,
                presence_penalty=None,
                tool_choice=None,
                parallel_tool_calls=None,
                truncation=None,
                max_tokens=None,
                reasoning=None,
                verbosity=None,
                metadata=None,
                store=None,
                include_usage=None,
                response_include=None,
                top_logprobs=None,
                extra_query=None,
                extra_body=None,
                extra_headers=None,
                extra_args=None
            ),
            input_guardrails=[],
            output_guardrails=[],
            output_type=None,
            hooks=None,
            tool_use_behavior='run_llm_again',
            reset_tool_choice=True
        ),
        raw_item=ResponseOutputMessage(
            id='__fake_id__',
            content=[ResponseOutputText(annotations=[], text='Your current location is Governor House Karachi.\n', type='output_text', logprobs=None)],
            role='assistant',
            status='completed',
            type='message'
        ),
        type='message_output_item'
    )

]
"""

# Jab bhi tool call hota tw aik class ati hai ToolCallItem. Yani tool call hua 


"""
# name mein hum apne function ka name change kar skty hain.by default openai agent sdk wo name rakhta hai apne function ka jo hum ny provide 
# kia hota hai function name.

# Description main hum likhty hain ky hmara function kia kar raha / os ki description kia hai.by default description empty hoti hai hum khud 
# provide krty hain description.

# Doc String hmarey function ky notes hoty hain ky function kia kar rha or kia return kar rha or es mein features kia kia hain.
# Doc string or comment main ye frk hai. doc string LLM ko bhi visible hoty hain or comment LLM ko vivsible nhi hoty. Ye dono developer ky liye 
# hoty hain. Yani doc string bnany ka faida develper ko hoga wo ye read kar ky smjh jaye ga ky funtion mein kia ho rha hai.
# Doc String Explanation( parameters,  return statement, erorr handling, Raises Example )

# name_overide,description_override or doc string hum ny apne LLM ky liye define ki hai ta ky wo osey or explicit ho kr dekhy. Ye teeno cheez 
# es liye dein gay hum kyu ky ye LLM ko vivible hoti hain or ye Provide karna es liye hoti hain kyu ky hum hmesha LLM ky bharose nhi rah skty
# apko apne end sy bhi strong code likhna parta hai. name overide, discription overide, doc string es ko hum strong code khein gay.

"""


"""
You can use any Python function as a tool. The Agents SDK will setup the tool automatically:

The name of the tool will be the name of the Python function (or you can provide a name)
Tool description will be taken from the docstring of the function (or you can provide a description)
The schema for the function inputs is automatically created from the function's arguments
Descriptions for each input are taken from the docstring of the function, unless disabled
"""

