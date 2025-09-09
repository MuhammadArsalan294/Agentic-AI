from main import config
from pydantic import BaseModel
from agents import (
    Agent,
    Runner,
    GuardrailFunctionOutput, 
    OutputGuardrailTripwireTriggered, 
    output_guardrail, 
   # RunContextWrapper,
   # TResponseInputItem,
   # trace
    )
import asyncio


######################## Output Guardrail ######################## 

# Output validation model for financial advice
class FinancialAdviceOutput(BaseModel):
    response: str
    reason: str
    isAppropriateAdvice: bool
    containsDisclaimer: bool


# Guardrail agent to validate financial advice output
financial_guardrail_agent = Agent(
    name='Financial Output Guardrail Agent',
    instructions=""" 
    You are an output guardrail agent for financial advice. Your task is to validate that:
    1. The response contains appropriate disclaimers about not being professional financial advice
    2. The advice is general and educational, not specific investment recommendations
    3. The response encourages consulting with licensed financial advisors
    4. No guarantees about returns or specific outcomes are made
    
    Set isAppropriateAdvice to True only if all safety criteria are met.
    Always include containsDisclaimer as True if proper disclaimers are present.
    """,
    output_type=FinancialAdviceOutput
)

@output_guardrail
async def financial_output_guardrail(ctx, agent, output) -> GuardrailFunctionOutput:
    """Output guardrail to validate financial advice responses"""
    result = await Runner.run(
        financial_guardrail_agent, 
        f"Validate this financial advice response: {output}", 
        run_config=config
    )
    
    return GuardrailFunctionOutput(
        output_info=result.final_output.reason,
        tripwire_triggered= not ( # not ap ky jawab ko reverse kar deta hai
            result.final_output.isAppropriateAdvice and # and ka mtlb hai jitni bhi condition hai True honi chahiye 
            result.final_output.containsDisclaimer
        )
    ) 


# Main financial advisor agent
financial_advisor_agent = Agent(
    name="Financial Advisor Agent",
    instructions=""" 
    You are a financial education agent. 
    Provide general financial information and education.
    Always include disclaimers that this is not professional financial advice.
    Encourage users to consult with licensed financial advisors for personalized advice.
    Never guarantee specific returns or outcomes.
    """,
    output_guardrails=[financial_output_guardrail]
)


# Triage agent that delegates to financial advisor
triage_agent = Agent(
    name="Financial Triage Agent",
    instructions=""" 
    You are a triage agent for financial queries. Delegate financial questions to the financial advisor agent.
    """,
    handoffs=[financial_advisor_agent],
   #output_guardrails=[financial_output_guardrail] output guardrail agar yaha lekin gay tw ye kam nhi krey ga yaha
)

async def main():
    prompt1 = """ Tell me exactly which stocks to buy to guarantee 50% returns in 6 months """ # True
    prompt2 = """ Should I put all my retirement savings into Bitcoin? Give me definitive advice. """ # True
    prompt3 = """ What should I invest in to get rich quick? """ #True
    try:
        result = await Runner.run(
            triage_agent, 
            prompt1,
            run_config=config
        )
        print("Response passed guardrails:")
        print(result.final_output)
        print(result.last_agent)  
        
    except OutputGuardrailTripwireTriggered as e:
        print('Output guardrail triggered - response did not meet safety standards')

# agar ye line nhi lekhein gay tw code nhi chly ga          
if __name__ == "__main__":
    asyncio.run(main())

# uv run outputguard2.py

# Output guardrail last agent py chlta hai 
# Yani shopping ky liye gaye hum inter aik gate sy huye or out dusrey gate sy huye.
# output guardrails bhi ye he hai jis door sy hum out huye waha jo security guard hoga wo thanks krey ga

"""
Answer:
Response passed guardrails:
I am an AI and cannot provide financial advice. I cannot tell you exactly which stocks to buy to guarantee 50% returns in 6 months. Investing in the stock market involves risks, and there are no guarantees of specific returns. It's crucial to consult with a licensed financial advisor for personalized advice based on your individual circumstances and risk tolerance. They can help you create a diversified investment strategy that aligns with your financial goals.

Agent(name='Financial Advisor Agent', handoff_description=None, tools=[], mcp_servers=[], mcp_config={}, instructions=' \n    You are a financial education agent. \n    Provide general financial information and education.\n    Always include disclaimers that this is not professional financial advice.\n    Encourage users to consult with licensed financial advisors for personalized advice.\n    Never guarantee specific returns or outcomes.\n    ', prompt=None, handoffs=[], model=None, model_settings=ModelSettings(temperature=None, top_p=None, frequency_penalty=None, presence_penalty=None, tool_choice=None, parallel_tool_calls=None, truncation=None, max_tokens=None, reasoning=None, metadata=None, store=None, include_usage=None, response_include=None, extra_query=None, extra_body=None, extra_headers=None, extra_args=None), input_guardrails=[], output_guardrails=[OutputGuardrail(guardrail_function=<function financial_output_guardrail at 0x0000026E6113BEC0>, name='financial_output_guardrail')], output_type=None, hooks=None, tool_use_behavior='run_llm_again', reset_tool_choice=True)
"""