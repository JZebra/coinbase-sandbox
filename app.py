from coinbase.wallet.client import Client

from config import coinbase_api_key, coinbase_api_secret

SANDBOX_URL = 'https://api.sandbox.coinbase.com'

client = Client(
    coinbase_api_key(),
    coinbase_api_secret(),
    base_api_uri=SANDBOX_URL)

accounts = client.get_accounts()
for account in accounts.data:
    balance = account.balance
    print "%s: %s %s" % (account.name, balance.amount, balance.currency)
    print account.get_transactions()

account = client.create_account(name="New Wallet")
balance = account.balance
print "%s: %s %s" % (account.name, balance.amount, balance.currency)

# Generate a new bitcoin address for your primary account:
primary_account = client.get_primary_account()
address = account.create_address() # You created this account in the previous step
print address


# Send coins to the new account from your primary account:
primary_account.send_money(
    to=address.address,
    amount='0.01',
    currency='BTC',
    description='For being awesome!')

# View the last transaction
print primary_account.get_transactions()[-1]

# After some time, the transaction should complete and your balance should update
primary_account.refresh()
balance = primary_account.balance
print "%s: %s %s" % (primary_account.name, balance.amount, balance.currency)
