# save this as app.py
from flask import Flask
from flask import render_template
import pandas as pd
import requests

app = Flask(__name__)
datacsv = "https://www.data.gouv.fr/fr/datasets/r/f4935ed4-7a88-44e4-8f8a-33910a151d42"


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/hello")
def hello(data=None):
    data = requests.get(datacsv).text
    return render_template('hello.html', data=data)
