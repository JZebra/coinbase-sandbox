from coinbase.wallet.client import Client

from config import coinbase_api_key, coinbase_api_secret

SANDBOX_URL = 'https://api.sandbox.coinbase.com'

client = Client(
    coinbase_api_key(),
    coinbase_api_secret(),
    base_api_uri=SANDBOX_URL)

payment_methods = client.get_payment_methods()

account = client.get_primary_account()
payment_method = client.get_payment_methods()[0]

buy_price_threshold = 200
sell_price_threshold = 500

buy_price = client.get_buy_price(currency='USD')
sell_price = client.get_sell_price(currency='USD')

if float(sell_price.amount) <= sell_price_threshold:
  sell = account.sell(amount='1',
                      currency="BTC",
                      payment_method=payment_method.id)

if float(buy_price.amount) <= buy_price_threshold:
  buy = account.buy(amount='1',
                    currency="BTC",
                    payment_method=payment_method.id)
