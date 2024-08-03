import ui_returns
import utilities
from datetime import date
from datetime import timedelta
from data import Data

 

def getCryptoData():
    coins = ["X:BTCUSD", "X:ETHUSD", "X:USDTUSD", "X:DOGEUSD", "X:SOLUSD", "X:USDCUSD", "X:XRPUSD", "X:SHIBUSD", "X:ADAUSD", "X:TRXUSD"]
    insert_crypto_data = Data(coins,"CRYPTO")
    insert_crypto_data.getData() 

def getForexData():
    f_currencies = ["C:EURUSD", "C:JPYUSD", "C:GBPUSD", "C:CNYUSD", "C:AUDUSD", "C:CADUSD", "C:CHFUSD", "C:HKDUSD", "C:NZDUSD"]
    insert_forex_data = Data(f_currencies,"FOREX")
    insert_forex_data.getData()

def getStocksData():
    f_currencies = ["AAPL","MSFT","NVDA","GOOG","AMZN","META","TSLA","CRM","AMD","INTC"]
    insert_forex_data = Data(f_currencies,"STOCKS")
    insert_forex_data.getData()


def main():

#run utilities and check api request limits on metals 
    utilities.create_tbl_utilitily()
    utilities.create_tbl_month1()
    utilities.create_tbl_month2()
    utilities.create_tbl_month3()
    #getCryptoData()
    #getForexData()
    #getStocksData()

    all_tickers = ui_returns.ticker_info('ETHUSD','CRYPTO','month1')
    ticker_list = ui_returns.ticker_list()
    print((f'''{all_tickers}\n{ticker_list}'''))
if __name__ == '__main__':
    main()
