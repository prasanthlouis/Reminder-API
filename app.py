#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for

app = Flask(__name__)

reminders = [
    {
        'id': 1,
        'title': u'Market',
        'desc': u'Chips and Dips', 
        'finish': False
    },
    {
        'id': 2,
        'title': u'Interview at 3 p.m',
        'desc': u'Get shirt ironed', 
        'finish': False
    },
     {
        'id': 3,
        'title': u'Meeting with the Boss',
        'desc': u'Bring the report', 
        'finish': False
    }

]

@app.route('/todo/api/v1/todoabc/<int:todoabc_id>', methods=['DELETE'])
def delete_todoabc(todoabc_id):
    todoabc = [todoabc for todoabc in reminders if todoabc['id'] == todoabc_id]
    if len(todoabc) == 0:
        abort(404)
    reminders.remove(todoabc[0])
    return jsonify({'result': True})

@app.route('/todo/api/v1/todoabc/<int:todoabc_id>', methods=['PUT'])
def update_todoabc(todoabc_id):
    todoabc = [todoabc for todoabc in reminders if todoabc['id'] == todoabc_id]
    if len(todoabc) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'desc' in request.json and type(request.json['desc']) is not unicode:
        abort(400)
    if 'finish' in request.json and type(request.json['finish']) is not bool:
        abort(400)
    todoabc[0]['title'] = request.json.get('title', todoabc[0]['title'])
    todoabc[0]['desc'] = request.json.get('desc', todoabc[0]['desc'])
    todoabc[0]['finish'] = request.json.get('finish', todoabc[0]['finish'])
    return jsonify({'todoabc': todoabc[0]})   

@app.route('/todo/api/v1/todoabc', methods=['POST'])
def create_todoabc():
    if not request.json or not 'title' in request.json:
        abort(400)
    todoabc = {
        'id': reminders[-1]['id'] + 1,
        'title': request.json['title'],
        'desc': request.json.get('desc', ""),
        'finish': False
    }
    reminders.append(todoabc)
    return jsonify({'listofreminders': reminders}), 201

@app.route('/todo/api/v1/todoabc', methods=['GET'])
def get_todolists():
    return jsonify({'todolists': [make_public_todoabc(todoabc) for todoabc in reminders]})

def make_public_todoabc(todoabc):
    new_todoabc = {}
    for field in todoabc:
        if field == 'id':
            new_todoabc['uri'] = url_for('get_todoabc', todoabc_id=todoabc['id'], _external=True)
        else:
            new_todoabc[field] = todoabc[field]
    return new_todoabc
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/todo/api/v1/todoabc/<int:todoabc_id>', methods=['GET'])
def get_todoabc(todoabc_id):
    todoabc = [todoabc for todoabc in reminders if todoabc['id'] == todoabc_id]
    if len(todoabc) == 0:
        abort(404)
    return jsonify({'todoabc': todoabc[0]})



if __name__ == '__main__':
    app.run(debug=True)