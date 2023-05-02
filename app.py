# main.py
 
from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    with open('./data.json') as json_file:
        data = json.load(json_file)
    print("data is ", data)
    return json.dumps(data)