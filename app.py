# main.py
from flask import Flask, render_template
import json
import random
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_line_data', methods=['GET'])
def new_line_data():
    datas = [
        [589, 445, 483, 503, 689, 692, 634],
        [10, 35, 83, 66, 54, 32, 98],
        [1, 12, 65, 33, 78, 100, 3],
        [54, 32, 65, 32, 34, 76, 8],
    ]
    index = random.randrange(4)
    return json.dumps(datas[index])

@app.route('/get_data')
def get_data():
    with open('./data.json') as json_file:
        data = json.load(json_file)
    return json.dumps(data)

# pie_data
# datas = [
#         [589, 445, 483],
#         [10, 35, 83],
#         [1, 12, 65],
#         [54, 32, 65],
#     ]