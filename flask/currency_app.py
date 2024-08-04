
from flask import Flask, render_template, request
import prices
import ui_returns

app = Flask(__name__)

@app.route("/")
def home():
    prices.main()
    get_range_info = request.args.get('range')
    print(get_range_info)
    range_info = ui_returns.range_info(get_range_info)
    data = []
    data.append(range_info)
    return render_template("index.html",data=data)