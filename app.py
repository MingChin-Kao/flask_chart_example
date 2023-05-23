# main.py
from flask import Flask, render_template
import json
import random
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="0000"
)

def query_db(query, args=(), one=False):
    cursor = conn.cursor()
    cursor.execute(query, args)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    datas = []
    for r in rows:
        data = dict()
        for i in range(len(cursor.description)):
            data[cursor.description[i][0]] = r[i]
        datas.append(data)
    return datas

def insert_or_update(query, args=(), one=False):
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    conn.close()
    return 'insert or update data'


@app.route('/query_data')
def query_data():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.users;")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(row)
    cursor.close()
    return str(result)


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