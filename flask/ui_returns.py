import sqlite3
import utilities

def all_investments(type,range):
    conn = sqlite3.connect('currencydb.db')
    cursor = conn.cursor()
    table = ''
    type = str(type)
    curr_month = utilities.get_date()
    curr_month = curr_month[f'curr_month_param1']
    if range == 'month1':
        table = 'MONTH1_TBL'
    elif range == 'month2':
        table = 'MONTH2_TBL'
    elif range ==  'month3':
        table = 'MONTH3_TBL'
    cursor.execute(f'''SELECT * FROM {table} WHERE type = "{type}" and modified = "{curr_month}"''')
    rows = cursor.fetchall()
    return rows

def ticker_info(ticker,type,range):
    conn = sqlite3.connect('currencydb.db')
    cursor = conn.cursor()
    table = ''
    type = str(type)
    ticker = str(ticker)
    curr_month = utilities.get_date()
    curr_month = curr_month[f'curr_month_param1']
    if range == 'month1':
        table = 'MONTH1_TBL'
    elif range == 'month2':
        table = 'MONTH2_TBL'
    elif range ==  'month3':
        table = 'MONTH3_TBL'
    cursor.execute(f'''SELECT * FROM {table} WHERE type = "{type}" and modified = "{curr_month}" and ticker = "{ticker}"''')
    rows = cursor.fetchall()
    return rows

def ticker_list():
    conn = sqlite3.connect('currencydb.db')
    cursor = conn.cursor()
    curr_month = utilities.get_date()
    curr_month = curr_month[f'curr_month_param1']
    cursor.execute('SELECT distinct ticker FROM MONTH1_TBL')
    rows = cursor.fetchall()
    ticker_list = []
    for row in rows:
        row = str(row)
        ticker_list.append(row.strip('"()"'))
    return ticker_list