#进阶函数版 不写if判断了,用url名字去找对应的函数名
import socket
sk=socket.socket()
sk.bind(('127.0.0.1',8001))
sk.listen()

# 定义一个处理/yimi/的函数
def yimi(url):
    ret = 'hello {}'.format(url)
    return bytes(ret, encoding="utf-8")


# 定义一个处理/xiaohei/的函数
def xiaohei(url):
    ret = 'hello {}'.format(url)
    return bytes(ret, encoding="utf-8")


# 定义一个专门用来处理404的函数
def f404(url):
    ret = "你访问的这个{} 找不到".format(url)
    return bytes(ret, encoding="utf-8")


url_func = [
    ("/yimi/", yimi),
    ("/xiaohei/", xiaohei),
]



while 1:
    conn,_=sk.accept()
    data=conn.recv(1024)
    data_str=str(data,encoding='utf-8')
    l1=data_str.splitlines()
    l2=l1[0].split()
    url=l2[1]
# 给客户端回复消息
    conn.send(b'http/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n')
    # 想让浏览器在页面上显示出来的内容都是响应正文

    # 根据不同的url返回不同的内容
    # 去url_func里面找对应关系
    for i in url_func:
        if i[0] == url:
            func = i[1]
            break
    # 找不到对应关系就默认执行f404函数
    else:
        func = f404
    # 拿到函数的执行结果
    response = func(url)
    # 将函数返回的结果发送给浏览器
    conn.send(response)




