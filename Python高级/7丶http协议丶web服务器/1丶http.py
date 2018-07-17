#（1）http请求
"""
1丶浏览器向服务器发送http请求，请求包括：
    方法：GET还是POST，GET仅请求资源，POST会附带用户数据；
    路径：/full/url/path；
    域名：由Host头指定：Host: www.sina.com  服务器主机地址
    以及其他相关的Header；
    如果是POST，那么请求还包括一个Body，包含用户数据

2丶服务器向浏览器返回http响应，响应包括

    响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误；
    响应类型：由Content-Type指定；请注意，浏览器就是依靠Content-Type来判断响应的内容是网页还是图片，是视频还是音乐。浏览器并不靠URL来判断响应的内容，所以，即使URL是http://www.baidu.com/meimei.jpg，它也不一定就是图片。
    以及其他相关的Header；
    通常服务器的HTTP响应会携带内容，也就是有一个Body，包含响应的内容，网页的HTML源码就在Body中。
"""

#（2）http格式
"""
1丶http get请求的格式：每个Header一行一个，换行符是\r\n。
    GET /path HTTP/1.1
    Header1: Value1
    Header2: Value2
    Header3: Value3
2丶http post请求的格式：当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body。
    POST /path HTTP/1.1
    Header1: Value1
    Header2: Value2
    Header3: Value3

    body data goes here...
3丶http响应的格式：HTTP响应如果包含body，也是通过\r\n\r\n来分隔的。
    200 OK
    Header1: Value1
    Header2: Value2
    Header3: Value3
    
    body data goes here...
"""

import socket
tcp_server_socket = socket.socket(socket.A)