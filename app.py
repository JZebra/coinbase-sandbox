from coinbase.wallet.client import Client

from config import coinbase_api_key, coinbase_api_secret

SANDBOX_URL = 'https://api.sandbox.coinbase.com'


client = Client(
    coinbase_api_key(),
    coinbase_api_secret,
    base_api_uri=SANDBOX_URL)
