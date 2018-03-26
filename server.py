import socket
import json
from routes.js_route import(todo_api_js, todo_js)
from routes.todo_api import (todo_add, todo_all)
from utils import *

class Request(object):

    def __init__(self):
        self.path = ''
        self.body = ''

    def json_to_dict(self):
        return json.loads(self.body)


def response_for_path(request):
    r = {
        '/': route_index,
        '/todo_api.js': todo_api_js,
        '/todo.js': todo_js,
        '/api/todo/all': todo_all,
        '/api/todo/add': todo_add,

    }
    path = request.path
    response = r.get(path, error)
    return response(request)


def run(host='', port=3000):
    """
    启动服务器
    """
    # 初始化 socket 套路
    # 使用 with 可以保证程序中断的时候正确关闭 socket 释放占用的端口
    log('start listening at 127.0.0.1:{}'.format(port))
    with socket.socket() as s:
        s.bind((host, port))
        # 无限循环来处理请求
        while True:
            # 监听 接受 读取请求数据 解码成字符串
            s.listen(5)
            connection, address = s.accept()
            request = connection.recv(1024)
            # log('raw, ', request)
            r = Request()
            request = request.decode('utf-8')
            log('ip and request, {}\n{}'.format(address, request))
            request_body = request.split('\r\n\r\n', 1)[1]
            r.body = request_body
            print(request_body)
            try:
                # 因为 chrome 会发送空请求导致 split 得到空 list
                # 所以这里用 try 防止程序崩溃
                path = request.split()[1]
                r.path = path
                # 用 response_for_path 函数来得到 path 对应的响应内容
                response = response_for_path(r)
                # 把响应发送给客户端
                connection.sendall(response)
            except Exception as e:
                log('error', e)
            # 处理完请求, 关闭连接
            connection.close()


def route_index(r):
    return render_html('test.html')






if __name__ == '__main__':
    run()
