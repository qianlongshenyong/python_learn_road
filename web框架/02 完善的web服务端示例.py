import socket

sk=socket.socket()
sk.bind(("127.0.0.1", 8001))
sk.listen()
while 1:
    # 获取与客户端的连接
    conn, _ = sk.accept()
    # 接收客户端发来消息
    data = conn.recv(8096)
    print(data.splitlines())
    # 给客户端回复消息
    conn.send(b'http/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n') #http协议的格式
    # 想让浏览器在页面上显示出来的内容都是响应正文
    conn.send(b'<h1>hello s10!</h1>')
    # 关闭

    conn.close()
  #  sk.close()  错误
# OSError: [WinError 10038] 在一个非套接字上尝试了一个操作。

# 每次循环的时候我把socket的客户端给关闭了

#注:  需要按照http协议发送内容给浏览器