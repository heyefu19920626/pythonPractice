### 网络编程
[TCP/IP](#tcp-ip)  
[TCP编程](#tcp-programe)

- 网络通信就是两个进程之间在通信

<div id="tcp-ip"></div>
### TCP/IP
- ip4
    - 32位整数，按八位分组后以字符串表示
- ip6
    + 128位整数
- 一个TCP报文除了要包含传输的数据以外，还包含源IP地址和目标IP地址，源端口和目标端口
- TCP协议则是建立在IP协议之上的
- 许多常用的更高级的协议都是建立在TCP协议基础上的

<div id="#tcp-programe"></div>

### TCP编程
- 服务器
```python
import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waitting for connection...')


def tcplink(sock, addr):
    print('Accept new connection form %s:%s...', addr)
    sock.send(b'Weclocme')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print('Receive %s from %s' % (data, addr))
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Cnnection from %s:%s closed.' % addr)


while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
```
- 客户端
```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tom', b'Tracy', b'Sarch']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
```