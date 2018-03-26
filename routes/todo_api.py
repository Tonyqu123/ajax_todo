import json
from mongo_orm import Todo
from utils import log


def todo_add(request):
    form = request.body #前端传过来的是json
    d = json.loads(form)
    name = d.get('title')
    t = Todo(title = name)
    t.save()
    print(t.__dict__.pop('_id'))
    return json_response(t.__dict__)


def todo_all(r):
    todo_list = Todo.all()
    return json_response(todo_list)


def json_response(data):
    header = 'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n'
    body = json.dumps(data, ensure_ascii=False, indent=2)
    print(body)
    response = header + '\r\n' + body
    return response.encode(encoding='utf-8')


