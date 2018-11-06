from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/linechart")
def linechart():
    """
    https://bl.ocks.org/gordlea/27370d1eea8464b04538e6d8ced39e89
    :return:
    """
    return render_template("linechart.html")

app.run(port=5500, debug=True)