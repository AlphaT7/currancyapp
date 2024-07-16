import requests
import json
import sqlite3

conn = sqlite3.connect('currencydb.db')

conn.execute('''CREATE TABLE IF NOT EXISTS MONTH1_TBL
         (ID INTEGER,
         TICKER           TEXT           NOT NULL,
         JSON             VARCHAR(10)    NOT NULL,
         PRIMARY KEY("ID" AUTOINCREMENT));''')
conn.close()

def getCryptoData():
    coin = ["BTCUSD", "ETHUSD", "USDTUSD", "BNBUSD", "SOLUSD", "USDCUSD", "XRPUSD", "DOGEUSD", "ADAUSD", "TRXUSD"]
    multiplier = 1
    timespan = 'day'
    date_from = '2023-01-09'
    date_to = '2023-02-10'
    adjusted = True
    soft = 'Asc'
    url = 'https://api.polygon.io/v2/aggs/ticker/X:BTCUSD/range/1/day/2023-01-09/2023-02-10?adjusted=true&sort=asc&apiKey=A_fkKUzAMb5pppLVgBubk8cP5pF1T8m3'
    response = requests.get(url)
    crypto_data = json.loads(response.text)
    print(crypto_data)
    conn = sqlite3.connect('currencydb.db')
    cursor = conn.cursor()
    sqlite_insert_with_param = '''INSERT INTO MONTH1_TBL (TICKER,JSON) VALUES(?,?)'''
    crypto_data_to_save = (coin[0] ,str(crypto_data))
    cursor.execute(sqlite_insert_with_param,crypto_data_to_save)
    conn.commit()
    conn.close()


def getForexData():
    forex_ticker = ["C:EURUSD", "EUR", "JPY", "GBP", "CNH", "AUD", "CAD", "CHF", "HKD", "NZD"]
    multiplier = 1
    timespan = 'day'
    date_from = '2023-01-09'
    date_to = '2023-02-10'
    adjusted = True
    soft = 'Asc'
    url = 'https://api.polygon.io/v2/aggs/ticker/C:EURUSD/range/1/day/2023-01-09/2023-02-10?adjusted=true&sort=asc&apiKey=A_fkKUzAMb5pppLVgBubk8cP5pF1T8m3'
    response = requests.get(url)
    forex_data = json.loads(response.text)
    print(forex_data)
    conn = sqlite3.connect('currencydb.db')
    cursor = conn.cursor()
    sqlite_insert_with_param = '''INSERT INTO MONTH1_TBL (TICKER,JSON) VALUES(?,?)'''
    forex_data_to_save = (forex_ticker[0] ,str(forex_data))
    cursor.execute(sqlite_insert_with_param,forex_data_to_save)
    conn.commit()
    conn.close()


def get_gold_data():
    api_key = "goldapi-5kaslyj55d1l-io"
    symbol = "XAU"
    curr = "USD"
    date = ""

    url = f"https://www.goldapi.io/api/{symbol}/{curr}{date}"
    
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    gold_data = json.loads(response.text)
    print(gold_data)
    conn = sqlite3.connect('currencydb.db')
    cursor = conn.cursor()
    sqlite_insert_with_param = '''INSERT INTO MONTH1_TBL (TICKER,JSON) VALUES(?,?)'''
    gold_data_to_save = (symbol ,str(gold_data))
    cursor.execute(sqlite_insert_with_param,gold_data_to_save)
    conn.commit()
    conn.close()


def main():
    getCryptoData()
    get_gold_data()
    getForexData()
    # errors = []
    # try:
    #     getCurrencyData()
    # except requests.exceptions.RequestException as e:
    #     errors.append(("Error:", str(e)))
    # try:
    #     get_gold_data()
    # except requests.exceptions.RequestException as e:
    #     errors.append(("Error:", str(e)))
    # try:
    #     getForexData()
    # except requests.exceptions.RequestException as e:
    #     errors.append(("Error:", str(e)))
    # return errors
    
if __name__ == '__main__':
    main()
