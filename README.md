# Reminder-API
A REST-API implemented with Python, Flask and Curl


To start, use ./app.py

Access Tasks: curl -u prasanth:password -i http://localhost:5000/todo/api/v1/todoabc

Access Taks by id: curl  -u prasanth:password -i http://localhost:500/todo/api/v1/todoabc/id
(It'll display when you use the general todoabc)

If it's not found an error will be returned in JSON

UPDATE:  curl -i -H "Content-Type: application/json" -X PUT -d '{"finish":true}' http://localhost:5000/todo/api/v1/todoabc/2

INSERT: curl -i -H "Content-Type: application/json" -X POT -d '{"title":"Fun in the Sun"}' http://localhost:5000/todo/api/v1/todoabc

DELETE curl -X DELETE http://localhost:5000/todo/api/v1/todoabc/3
