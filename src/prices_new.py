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
    url = 'https://open.er-api.com/v6/latest/USD'
    response = requests.get(url)
    currency_data = json.loads(response.text)
    top_ten_currency = ["USD", "EUR", "JPY", "GBP", "CNH", "AUD", "CAD", "CHF", "HKD", "NZD"]
    top_currency = []
    for currency in currency_data['rates']:
        if currency in top_ten_currency:
            top_currency.append(currency)
    return top_currency

def main():
    UIData = []
    UIData.append(getCryptoData())
    UIData.append(getCurrencyData())
    return UIData
    
if __name__ == '__main__':
    main()