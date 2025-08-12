from agents import Agent, Runner, function_tool # agent bnany or run karne k liye use kia hai 
from main import config # import module ye main file sy import kia
import requests # Ye Python ka built-in module hai jo API requests bhejne ke liye use hota hai.


@function_tool
def get_crypto_price(coin: str = "bitcoin", currency: str = "usd") -> str:
    """
    Gets the current price of a cryptocurrency. # Ye API se current price fetch kar raha hai CoinGecko ki
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"
    response = requests.get(url)
    data = response.json() 

    if coin in data and currency in data[coin]: 
        price = data[coin][currency] # Agar coin + currency dono mil jayein: Price return karo readable format mein.
        return f"The current price of {coin.capitalize()} is {price} {currency.upper()}."
    else:
        return "Cryptocurrency not found or API error."

crypto_agent = Agent(
    name="Crypto Price Agent",
    instructions="""
        You are a helpful Crypto Price Assistant.
        Use the 'get_crypto_price' tool to get real-time prices of cryptocurrencies.

        If the user doesn't mention the currency, assume 'usd' as default.
        If the user doesn't mention the coin, assume 'bitcoin' as default.

        Respond clearly in a friendly tone.
    """,
    tools=[get_crypto_price]
)

result = Runner.run_sync(
    crypto_agent,
    "Current Price Of Bitcoin",
   run_config=config
)


print(result.final_output) 

# uv run cryptoagents.py





