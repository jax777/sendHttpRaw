#!/usr/bin/python3
# coding: utf-8


import socket, ssl
import struct
def sendhttps(host,port,raw,i):
    #print(raw)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.verify_mode = ssl.CERT_NONE
    context.check_hostname = False
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = context.wrap_socket(s, server_hostname=host)
    ssl_sock.connect((host, port))
    ssl_sock.send(raw)
    response = ssl_sock.recv()
    #print(response)
    print(i,chr(i),response[:30])
    #if b'HTTP/1.1 200 ' in response:
        #print(i)
        #print(response[:30])

def sendhttp(host,port,raw,i):
    #print(raw)
    tcpsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsoc.connect((host, port)) 
    tcpsoc.send(raw)
    tcpsoc.settimeout(1)
    try:
        response = tcpsoc.recv(1024)
        #print(response)
        tcpsoc.close()
        print(i,chr(i),response[:1024])
    except Exception as e:
        print(i,chr(i),e)



raw0 = b'''GET /getSpiderInfo/1.0'''
raw1 = b''' HTTP/1.1
Host: www.test.com
Connection: close
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
Accept: */*
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9



'''

#sendhttp(raw0+struct.pack("B", 68)+raw1,10)
for i in range(1,255):
    sendhttp('localhost',8080,raw0+struct.pack("B", i)+raw1,i)
