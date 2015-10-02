#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request

app = Flask(__name__)

reminders = [
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

@app.route('/todo/api/v1/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in reminders if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    reminders.remove(task[0])
    return jsonify({'result': True})

@app.route('/todo/api/v1/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in reminders if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})   

@app.route('/todo/api/v1/task', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': reminders[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    reminders.append(task)
    return jsonify({'listofreminders': reminders}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/todo/api/v1/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in reminders if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1/task', methods=['GET'])
def get_reminders():
    return jsonify({'listofreminders': reminders})

if __name__ == '__main__':
    app.run(debug=True)