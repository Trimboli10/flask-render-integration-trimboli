from flask import Flask, request, render_template
from utils import load_model, make_forecast
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = load_model(os.path.join(BASE_DIR, "..", "models", "series-temporales-trimboli.sav"))

@app.route("/", methods=["GET", "POST"])
def index():
    forecast_data = None
    steps = 30

    if request.method == "POST":
        steps = int(request.form["steps"])
        forecast_data = make_forecast(model, steps)

    return render_template("index.html", forecast=forecast_data, steps=steps)