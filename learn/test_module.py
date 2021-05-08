from learn import modules
import socket
import uuid


modules.test()

# 获取本机IP的方法


# 1. 通过hostname
# 有的机器没有规范hostname的设置

# 获取本机电脑名
myname = socket.getfqdn(socket.gethostname())
print(myname)
# 获取本机IP
myaddr = socket.gethostbyname(myname)
print(myaddr)

# 2. 通过UDP获取
# 生成一个UDP包，把自己的 IP 放如到 UDP 协议头中，然后从UDP包中获取本机的IP
# 并不会真实的向外部发包,但是会申请一个 UDP 的端口


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()
    finally:
        s.close()
    return ip


print(get_host_ip())

# 获取MAC地址


def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ':'.join([mac[e:e+2] for e in range(0, 11, 2)])


print(get_mac_address())
