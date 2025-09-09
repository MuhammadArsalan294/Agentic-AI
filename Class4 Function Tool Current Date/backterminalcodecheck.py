from agents import Agent, Runner, function_tool # funtion tool agent k module sy a rha hi
from main import config # import module ye main file sy import kia
from datetime import datetime
import rich # uv add rich terminal py  output read able krne k liye use krty hain ye or ye libray sy import kia hai

@function_tool # jitne bhi function bnao gay untny he decorator bhi lgao gy
def get_weather(city:str)->str:
    return f"the weather of {city} is rainy"

@function_tool#Decorator bhi function hoty hein  Decorator lga kar function ko tool bna dia or upper es ko import bhi kia hai
def get_date(): # ye simple function bnaya hai
    _now = datetime.now() # now means abhi
    return _now.strftime("the date is %d-%m-%Y")

@function_tool
def multiply(num1: int, num2: int)->int: # Parameter
    return num1 * num2  

# / Openai Agents SDK / uv add openai-agents 
agent = Agent( 
    name = "Assistant", # ye required parameter hai
    instructions = "You are a helpful assistant.",
    tools = [get_date, get_weather, multiply] # ye upper sy aya hai or yaha function ka name likha hai 
)

result = Runner.run_sync(
    agent,
    '5 multiply by 10', # pompt / augruments
    run_config=config
)

rich.print(result.new_items) # jasey run_sync sy final_output ata hai asey he new_items bhi hai
print(result.final_output) #final ouput string mein return krey ga means answer string mein dy ga

# uv run backterminalcodecheck.py

# hmarey jitne bhi function hain wo function tool return kr rha hai OR json form main a 
# rhi hai properties/parameter LLM sy
# LLM ky pass query gai os ny parameter ko extract kia or json form mein extract krey ga 
# parameter ko or json return hogi jo LLM ny function chosee kia hoga osko kaha sy mere
# prompt mein sy
#                                                  OR
# hmara Query LLM ky pass jaye gi JSON form mein kha sy hmara function mein sy jo 
# Function tool return kar rha hai

# Answer:
""" 
[
    ToolCallItem(
        agent=Agent(
            name='Assistant',
            handoff_description=None,
            tools=[
                FunctionTool(
                    name='get_date',
                    description='',
                    params_json_schema={
                        'properties': {},
                        'title': 'get_date_args',     
                        'type': 'object',
                        'additionalProperties': False,
                        'required': []
                    },
                    on_invoke_tool=<function
function_tool.<locals>._create_function_tool.<locals>._on_invoke_tool at 0x0000023701BBD940>, 
                    strict_json_schema=True,
                    is_enabled=True
                ),
                FunctionTool(
                    name='get_weather',
                    description='',
                    params_json_schema={
                        'properties': {'city': {'title': 'City', 'type': 'string'}},
                        'required': ['city'],
                        'title': 'get_weather_args',
                        'type': 'object',
                        'additionalProperties': False
                    },
                    on_invoke_tool=<function
function_tool.<locals>._create_function_tool.<locals>._on_invoke_tool at 0x0000023701BBD4E0>, 
                    strict_json_schema=True,
                    is_enabled=True
                ),
                FunctionTool(
                    name='multiply',
                    description='',
                    params_json_schema={
                        'properties': {
                            'num1': {'title': 'Num1', 'type': 'integer'},
                            'num2': {'title': 'Num2', 'type': 'integer'}
                        },
                        'required': ['num1', 'num2'],
                        'title': 'multiply_args',
                        'type': 'object',
                        'additionalProperties': False
                    },
                    on_invoke_tool=<function
function_tool.<locals>._create_function_tool.<locals>._on_invoke_tool at 0x0000023701BBDD00>, 
                    strict_json_schema=True,
                    is_enabled=True
                )
            ],
            mcp_servers=[],
            mcp_config={},
            instructions='You are a helpful assistant.',
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
                metadata=None,
                store=None,
                include_usage=None,
                response_include=None,
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
        raw_item=ResponseFunctionToolCall(
            arguments='{"num1":5,"num2":10}',
            call_id='',
            name='multiply',
            type='function_call',
            id='__fake_id__',
            status=None
        ),
        type='tool_call_item'
    ),
    ToolCallOutputItem(
        agent=Agent(
            name='Assistant',
            handoff_description=None,
            tools=[
                FunctionTool(
                    name='get_date',
                    description='',
                    params_json_schema={
                        'properties': {},
                        'title': 'get_date_args',
                        'type': 'object',
                        'additionalProperties': False,
                        'required': []
                    },
                    on_invoke_tool=<function
function_tool.<locals>._create_function_tool.<locals>._on_invoke_tool at 0x0000023701BBD940>, 
                    strict_json_schema=True,
                    is_enabled=True
                ),
                FunctionTool(
                    name='get_weather',
                    description='',
                    params_json_schema={
                        'properties': {'city': {'title': 'City', 'type': 'string'}},
                        'required': ['city'],
                        'title': 'get_weather_args',
                        'type': 'object',
                        'additionalProperties': False
                    },
                    on_invoke_tool=<function
function_tool.<locals>._create_function_tool.<locals>._on_invoke_tool at 0x0000023701BBD4E0>, 
                    strict_json_schema=True,
                    is_enabled=True
                ),
                FunctionTool(
                    name='multiply',
                    description='',
                    params_json_schema={
                        'properties': {
                            'num1': {'title': 'Num1', 'type': 'integer'},
                            'num2': {'title': 'Num2', 'type': 'integer'}
                        },
                        'required': ['num1', 'num2'],
                        'title': 'multiply_args',
                        'type': 'object',
                        'additionalProperties': False
                    },
                    on_invoke_tool=<function
function_tool.<locals>._create_function_tool.<locals>._on_invoke_tool at 0x0000023701BBDD00>, 
                    strict_json_schema=True,
                    is_enabled=True
                )
            ],
            mcp_servers=[],
            mcp_config={},
            instructions='You are a helpful assistant.',
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
                metadata=None,
                store=None,
                include_usage=None,
                response_include=None,
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
        raw_item={'call_id': '', 'output': '50', 'type': 'function_call_output'},
        output=50,
        type='tool_call_output_item'
    ),
    MessageOutputItem(
        agent=Agent(
            name='Assistant',
            handoff_description=None,
            tools=[
                FunctionTool(
                    name='get_date',
                    description='',
                    params_json_schema={
                        'properties': {},
                        'title': 'get_date_args',
                        'type': 'object',
                        'additionalProperties': False,
                        'required': []
                    },
                    on_invoke_tool=<function
function_tool.<locals>._create_function_tool.<locals>._on_invoke_tool at 0x0000023701BBD940>, 
                    strict_json_schema=True,
                    is_enabled=True
                ),
                FunctionTool(
                    name='get_weather',
                    description='',
                    params_json_schema={
                        'properties': {'city': {'title': 'City', 'type': 'string'}},
                        'required': ['city'],
                        'title': 'get_weather_args',
                        'type': 'object',
                        'additionalProperties': False
                    },
                    on_invoke_tool=<function
function_tool.<locals>._create_function_tool.<locals>._on_invoke_tool at 0x0000023701BBD4E0>, 
                    strict_json_schema=True,
                    is_enabled=True
                ),
                FunctionTool(
                    name='multiply',
                    description='',
                    params_json_schema={
                        'properties': {
                            'num1': {'title': 'Num1', 'type': 'integer'},
                            'num2': {'title': 'Num2', 'type': 'integer'}
                        },
                        'required': ['num1', 'num2'],
                        'title': 'multiply_args',
                        'type': 'object',
                        'additionalProperties': False
                    },
                    on_invoke_tool=<function
function_tool.<locals>._create_function_tool.<locals>._on_invoke_tool at 0x0000023701BBDD00>, 
                    strict_json_schema=True,
                    is_enabled=True
                )
            ],
            mcp_servers=[],
            mcp_config={},
            instructions='You are a helpful assistant.',
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
                metadata=None,
                store=None,
                include_usage=None,
                response_include=None,
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
            content=[
                ResponseOutputText(
                    annotations=[],
                    text='The result is 50.\n',
                    type='output_text',
                    logprobs=None
                )
            ],
            role='assistant',
            status='completed',
            type='message'
        ),
        type='message_output_item'
    )
]
The result is 50.
"""