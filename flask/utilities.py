import sqlite3
from datetime import date, datetime, timedelta
from monthdelta import monthdelta


def create_tbl_month1():

    conn = sqlite3.connect('currencydb.db')

    conn.execute('''CREATE TABLE IF NOT EXISTS MONTH1_TBL
            (ID INTEGER,
            TYPE             TEXT           NOT NULL,
            TICKER           TEXT           NOT NULL,
            JSON             VARCHAR(10)    NOT NULL,
            MODIFIED         TEXT           NOT NULL,
            PRIMARY KEY("ID" AUTOINCREMENT));''')
    conn.close()

def create_tbl_month2():

    conn = sqlite3.connect('currencydb.db')

    conn.execute('''CREATE TABLE IF NOT EXISTS MONTH2_TBL
            (ID INTEGER,
            TICKER           TEXT           NOT NULL,
            TYPE             TEXT           NOT NULL,
            JSON             VARCHAR(10)    NOT NULL,
            MODIFIED         TEXT           NOT NULL,
            PRIMARY KEY("ID" AUTOINCREMENT));''')
    conn.close()

def create_tbl_month3():
    
    conn = sqlite3.connect('currencydb.db')

    conn.execute('''CREATE TABLE IF NOT EXISTS MONTH3_TBL
            (ID INTEGER,
            TICKER           TEXT           NOT NULL,
            TYPE             TEXT           NOT NULL,
            JSON             VARCHAR(10)    NOT NULL,
            MODIFIED         TEXT           NOT NULL,
            PRIMARY KEY("ID" AUTOINCREMENT));''')
    conn.close()

def create_tbl_utilitily():
    
    conn = sqlite3.connect('currencydb.db')

    conn.execute('''CREATE TABLE IF NOT EXISTS UTIL_TBL
            (ID INTEGER,
            CALLS            TEXT           NOT NULL,
            API              TEXT           NOT NULL,
            ERRORLOG         VARCHAR(10)    NOT NULL,
            MODIFIED         TEXT           NOT NULL,
            PRIMARY KEY("ID" AUTOINCREMENT));''')
    conn.close()

def get_date():
    now = datetime.now()
    date_params = {}
    for month in range(1,4):
        last_month = now - monthdelta(month)
        date_params['curr_month_param'+''+str(month)] = now.strftime("%Y-%m-%d")
        date_params['prev_month_param'+''+str(month)] = last_month.strftime("%Y-%m-%d")
    return date_params

def get_yesterday():
    today = date.today()
    yesterday = today - timedelta(days = 1)
    return yesterday

def api_calls_count(count,api,error):
    print(count)
    conn = sqlite3.connect('currencydb.db')
    cursor = conn.cursor()
    today = date.today()
    sqlite_insert_with_param = '''INSERT INTO UTIL_TBL (CALLS,API,ERRORLOG,MODIFIED) VALUES(?,?,?,?)'''
    api_data_to_save = (count,api,error,today)
    cursor.execute(sqlite_insert_with_param,api_data_to_save)
    conn.commit()
    conn.close()



