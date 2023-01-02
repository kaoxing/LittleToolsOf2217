import socket

from threading import Thread


class Server(Thread):
    def run(self):
        s = socket.socket()
        host = '127.0.0.1'
        port = 8888
        s.bind((host, port))
        s.listen(8)
        while True:
            conn, addr = s.accept()
            while True:
                data = conn.recv(2048).decode()
                if data:
                    print("收到")
                    print(data)
                    conn.send(data.encode())
                else:
                    conn.close()
                    break


class Client(Thread):
    def run(self):
        c = socket.socket()  # 创建socket对象
        host = '127.0.0.1'  # 设置本地主机
        port = 8888  # 设置端口号
        c.connect((host, port))
        mess = input('你将要对服务端做什么？').encode()
        c.send(mess)
        data = c.recv(2048)
        print(data)
        c.close()


if __name__ == '__main__':
    print("here")
    t1 = Server()
    t2 = Client()
    t1.start()
    t2.start()

