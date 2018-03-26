def log(*args, **kwargs):
    print('*log*', *args, **kwargs)


def add_header(body):
    header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n'
    return header + '\r\n' + body


def render_html(html):
    with open('template/{}'.format(html), 'r', encoding='utf-8') as f:
        content = f.read()
        return add_header(content).encode(encoding='utf-8')


def error(code=404):
    e = {
        404: b'HTTP/1.1 404 NOT FOUND\r\n\r\n<h1>NOT FOUND</h1>'
    }
    return e.get(code, b'')
