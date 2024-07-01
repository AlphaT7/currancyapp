import requests
import json

def getCryptoData():
    #Crypto api request
    url = 'https://api.coincap.io/v2/assets'
    response = requests.get(url)
    crypto_data= json.loads(response.text)
    top_ten_crypto = ["BTC", "ETH", "USDT", "BNB", "SOL", "USDC", "XRP", "DOGE", "ADA", "TRX"]
    top_crypto = []
    for crypto in crypto_data['data']:
        if crypto['symbol'] in top_ten_crypto:
            top_crypto.append(crypto)
    return top_crypto

def getCurrencyData():
    # Currency api request
    # Where USD is the base currency you want to use
    url = 'https://open.er-api.com/v6/latest/USD'

    # Making our request
    response = requests.get(url)
    currency_data = response.json()
    # Your JSON object
    print(currency_data)
    return currency_data

def main():
    UIData = []
    UIData.append(getCryptoData())
    UIData.append(getCurrencyData())
    return UIData
    
if __name__ == '__main__':
    main()
