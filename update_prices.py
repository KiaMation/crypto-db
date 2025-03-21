import json
import requests
from datetime import datetime

# GitHub Configuration
GITHUB_FILE = "prices.json"

# coins to fetch prices for
COINS = {
    "BTC": {
        "CoinPaprika": "https://api.coinpaprika.com/v1/tickers/btc-bitcoin",
        "CoinGecko": "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd",
        "KuCoin": "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT",
        "Bitfinex": "https://api-pub.bitfinex.com/v2/ticker/tBTCUSD"
    },
    "ETH": {
        "CoinPaprika": "https://api.coinpaprika.com/v1/tickers/eth-ethereum",
        "CoinGecko": "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd",
        "KuCoin": "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=ETH-USDT",
        "Bitfinex": "https://api-pub.bitfinex.com/v2/ticker/tETHUSD"
    },
    "DOGE": {
        "CoinPaprika": "https://api.coinpaprika.com/v1/tickers/doge-dogecoin",
        "CoinGecko": "https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd",
        "KuCoin": "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=DOGE-USDT",
        "Bitfinex": "https://api-pub.bitfinex.com/v2/ticker/tDOGEUSD"
    }
}

def get_utc_timestamp():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

def fetch_prices():
    prices = {}

    for coin, sources in COINS.items():
        prices[coin] = []
        for source, url in sources.items():
            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()

                # extract the price from the response
                if source == "CoinPaprika":
                    price = data["quotes"]["USD"]["price"]
                elif source == "CoinGecko":
                    price = data[list(data.keys())[0]]["usd"]
                elif source == "KuCoin":
                    price = float(data["data"]["price"])
                elif source == "Bitfinex":
                    price = float(data[6])  # Index 6 holds the last price
                else:
                    continue
                
                prices[coin].append({
                    "price": price,
                    "source": source,
                    "timestamp": get_utc_timestamp()
                })
            except Exception as e:
                print(f"⚠️ Error fetching {coin} from {source}: {e}")

    return prices

def save_prices_locally():
    new_data = fetch_prices()

    try:
        with open(GITHUB_FILE, "r") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}

    for coin, values in new_data.items():
        if coin not in existing_data:
            existing_data[coin] = []
        existing_data[coin].extend(values)

    with open(GITHUB_FILE, "w") as file:
        json.dump(existing_data, file, indent=4)

# run the script
save_prices_locally()
