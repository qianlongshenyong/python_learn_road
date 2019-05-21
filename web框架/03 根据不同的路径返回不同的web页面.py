import socket

sk=socket.socket()
sk.bind(("127.0.0.1",8001))
sk.listen()
while 1:
    conn,_=sk.accept()
    data = conn.recv(8096)
    print(data)
    #接收到的数据是byte类型，需要转换为str类型
    data_str = str(data, encoding="utf-8")  # bytes("str", enconding="utf-8")
    # 用\r\n去切割上面的字符串
    print(data_str)
   # l1 = data_str.split("\r\n")
    l1=data_str.splitlines()  #与上面的按照（'\r\n'）分割的效果相同
    #循环打印列表
    for i in l1:
        print(i)
    # 按照空格切割上面的字符串
    l2 = l1[0].split()
    print(l2)
    url = l2[1]
    print(url)
    # 给客户端回复消息
    conn.send(b'http/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n')
    # 想让浏览器在页面上显示出来的内容都是响应正文

    # 根据不同的url返回不同的内容
    # 在浏览器中输入http://127.0.0.1:8001/name/
    if url == "/name/":
        response = b'<h1>my name is peter</h1>'

    #在浏览器中输入http://127.0.0.1:8001/xiaohei/
    elif url == "/xiaohei/":
        response = b'<h1>hello xiaohei!</h1>'
    else:
        response = b'<h1>404! not found!</h1>'
    conn.send(response)
    # 关闭
    conn.close()
#ctrl +tab 页面切换