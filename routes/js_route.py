
def todo_api_js(r):
    header = 'HTTP/1.1 200 OK\r\ncontent-type: application/javascript\r\n'
    with open('./static/todo_api.js', 'r', encoding='utf-8') as f:
        body = f.read()
    result = header + '\r\n' + body
    return result.encode(encoding='utf-8')


def todo_js(r):
    header = 'HTTP/1.1 200 OK\r\ncontent-type: application/javascript\r\n'
    with open('./static/todo.js', 'r', encoding='utf-8') as f:
        body = f.read()
    result = header + '\r\n' + body
    return result.encode(encoding='utf-8')

