
from flask import Flask, render_template, request
import prices
import ui_returns

app = Flask(__name__)

@app.route("/")
def home():
<<<<<<< HEAD
    # prices.main()
=======
    #prices.main()
>>>>>>> 265107ad07eb55b0dc91ad3131221551277a1f5d
    print('Welcome')
    return render_template("index.html")

@app.route("/tickers/")
def all_tickers():
    tickers = ui_returns.ticker_list()
    data = []
    data.append(tickers)
    return data

@app.route("/prices/<range>")
def all_prices(range):
    range_info = ui_returns.range_info(range)
    print(range_info)
    data = []
    data.append(range_info)
    return data