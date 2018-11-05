from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/linechart")
def linechart():
    return render_template("linechart.html")

app.run(port=5500, debug=True)