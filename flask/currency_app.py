
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # """
    # Home page route
    # """
    # if request.method == 'POST':
    #     message = request.form['message']
    #     return jsonify(your_message=message)
    return render_template("index.html")