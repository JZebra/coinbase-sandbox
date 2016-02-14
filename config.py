import yaml

with open('access_keys.yaml', 'r') as f:
    keys = yaml.load(f)
    COINBASE_API_KEY = keys.get('coinbase_api_key')
    COINBASE_API_SECRET = keys.get('coinbase_api_secret')


def coinbase_api_key():
    return COINBASE_API_KEY


def coinbase_api_secret():
    return COINBASE_API_SECRET
