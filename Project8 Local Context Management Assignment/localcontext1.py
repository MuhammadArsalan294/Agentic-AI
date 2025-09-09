from main import config
from pydantic import BaseModel 
from agents import(
    Agent,
    Runner,
    RunContextWrapper, 
    function_tool
)
import asyncio
import rich # uv add rich

# ------------------ Model ------------------
class BankAccount(BaseModel): 
    account_number: str
    customer_name: str
    account_balance: float
    account_type: str

bank_account = BankAccount(
    account_number="ACC-789456",
    customer_name="Ahmed",
    account_balance=75500.50,
    account_type="savings"
)

# ------------------ Tool ------------------
@function_tool  
def get_user_info(wrapper: RunContextWrapper[BankAccount]): 
    acc = wrapper.context
    return {
        "customer_name": acc.customer_name,
        "account_balance": acc.account_balance,
        "account_type": acc.account_type
    }
    # OR f"Customer {acc.customer_name} has a {acc.account_type} account with balance {acc.account_balance}"

# ------------------ Agent ------------------
personal_agent = Agent(
    name = "Personal Agent",
    instructions="You are a banking assistant. Use get_user_info to give account details.",
    tools = [get_user_info]
)

# ------------------ Runner ------------------
async def main():
    result = await Runner.run( 
        starting_agent = personal_agent,
        input="Tell me the account details.",
        run_config = config,
        context = bank_account # local context
    )
    rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

# uv run localcontext1.py   run this command line