#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Market',
        'description': u'Chips and Dips', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Interview at 3 p.m',
        'description': u'Get shirt ironed', 
        'done': False
    },
     {
        'id': 3,
        'title': u'Meeting with the Boss',
        'description': u'Bring the report', 
        'done': False
    }

]

@app.route('/todo/api/v1/task', methods=['GET'])
def get_tasks():
    return jsonify({'listoftasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)