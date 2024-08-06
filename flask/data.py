
import datetime
import requests
import json
import sqlite3
import utilities
import time
from requests.structures import CaseInsensitiveDict


class Data():
    def __init__(self,tickers,type):
        self.tickers = tickers
        self.type = type
    def getData(self):
        count = 1
        dt_count = 1
        tbls = ['MONTH1','MONTH2','MONTH3']
        url = ''
        for tbl in tbls:
            date_params = utilities.get_date()     
            date_param1 = date_params[f'curr_month_param{dt_count}']
            date_param2 = date_params[f'prev_month_param{dt_count}']
            for ticker in self.tickers:
                time.sleep(20)
                url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{date_param2}/{date_param1}?adjusted=true&sort=asc&apiKey=A_fkKUzAMb5pppLVgBubk8cP5pF1T8m3" 
                response = requests.get(url)
                api_data = json.loads(response.text)
                print(api_data)
                if self.type != 'STOCKS':
                    ticker = ticker[2:]
                conn = sqlite3.connect('currencydb.db')
                cursor = conn.cursor()
                if count <= 10 and tbl == 'MONTH1':
                    sqlite_insert_with_param = '''INSERT INTO MONTH1_TBL (TYPE,TICKER,JSON,MODIFIED) VALUES(?,?,?,?)'''
                    api_data_to_save = (self.type,ticker,str(api_data),date_param1)
                    cursor.execute(sqlite_insert_with_param,api_data_to_save)   
                    print("data inserted in table 1")
                    conn.commit()
                elif count >= 11 and count <= 21 and tbl == 'MONTH2':
                    sqlite_insert_with_param = '''INSERT INTO MONTH2_TBL (TYPE,TICKER,JSON,MODIFIED) VALUES(?,?,?,?)'''
                    api_data_to_save = (self.type,ticker,str(api_data),date_param1)
                    cursor.execute(sqlite_insert_with_param,api_data_to_save)
                    print("data inserted in table 2")
                    conn.commit()
                elif count >= 21 and count <= 31 and tbl == 'MONTH3':
                    sqlite_insert_with_param = '''INSERT INTO MONTH3_TBL (TYPE,TICKER,JSON,MODIFIED) VALUES(?,?,?,?)'''
                    api_data_to_save = (self.type,ticker,str(api_data),date_param1)
                    cursor.execute(sqlite_insert_with_param,api_data_to_save)
                    print("data inserted in table 3")
                    conn.commit()
                count += 1
            dt_count += 1
        conn.close()

    


        