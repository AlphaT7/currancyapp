import requests

def getCryptoData():
    #Crypto api request
    url = 'https://api.coincap.io/v2/assets'
    response = requests.get(url)
    crypto_data= response.json()['data']
    print(crypto_data)
    return crypto_data

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