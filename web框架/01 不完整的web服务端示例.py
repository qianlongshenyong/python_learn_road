# 首先写一个web服务端示例
#本质socket服务端
import socket
#生成socket对象
sk=socket.socket()

#绑定ip 和端口号
sk.bind(("127.0.0.1", 8001))

#开启监听
sk.listen()

# 写一个死循环,一直等待客户端来连我
while 1:
    # 获取与客户端的连接
    conn, _ = sk.accept()   #_的含义：
    # 接收客户端发来消息
    data = conn.recv(8096)  #
    print(data)
    # 给客户端回复消息
    conn.send(b'<h1>hello s10!</h1>')
    # 关闭
    conn.close()
    # sk.close()

#OSError: [WinError 10038] 在一个非套接字上尝试了一个操作。

#每次循环的时候我把socket的客户端给关闭了

# b'GET / HTTP/1.1\r\n
# Host: 127.0.0.1:8001\r\n
# Connection: keep-alive\r\n
# Cache-Control: max-age=0\r\n
# Upgrade-Insecure-Requests: 1\r\n
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36\r\n
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n
# Accept-Encoding: gzip, deflate, br\r\n
# Accept-Language: zh-CN,zh;q=0.9\r\n\r\n'

