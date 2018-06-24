import datetime
from datetime import timedelta
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter
import base64
import re
import hashlib
import itertools
from functools import reduce


# datetime
now = datetime.datetime.now()
print(now)
# int 转datetime
dt = datetime.datetime(2019, 8, 19, 23, 24, 56)
print(dt)
# str 转datetime
dt = datetime.datetime.strptime('2019-9-8 18:5:34', '%Y-%m-%d %H:%M:%S')
print(dt)
print(datetime.datetime.now().strftime('%a, %b %d %H:%M'))
# timestap
print(now.timestamp())
print(datetime.datetime.utcfromtimestamp(now.timestamp()))
print(datetime.datetime.fromtimestamp(now.timestamp()))

# datetime加减
print(now - timedelta(hours=10))


# collections

# namedtuple
Point = namedtuple('Point', ('x', 'y'))
p = Point(3, 5)
print(p.x)
print(p.y)

# deque
deq = deque(['1', '2', '3'])
print(deq)
deq.appendleft('0')
deq.append('4')
print(deq)

# defaultdict
dic = defaultdict(lambda: 'default')
dic['key'] = 'value'
print(dic['key'])
print(dic['test'])

d = dict({'x': 1, 'z': 2, 'y': 3})
for x in d:
    print(x)
d = dict([('a', 1), ('c', 2), ('b', 3)])
print(d)


# Counter
pro = 'programming'
cou = Counter()
for p in pro:
    cou[p] += 1
print(cou)


class LastUpdateOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self.capacity = capacity

    def __setitem__(self, key, value):
        containKey = 1 if key in self else 0
        if len(self) - containKey >= self.capacity:
            first = self.popitem(last=False)
            print('remove: ', first)
        if containKey:
            del self[key]
            print('set: ', (key, value))
        else:
            print('add: ', (key, value))
        OrderedDict.__setitem__(self, key, value)


last = LastUpdateOrderedDict(2)
last['a'] = 1
last['b'] = 2
print(last)
last['c'] = 3
print(last)
last['b'] = 4
print(last)


# base64
str_encode = base64.b64encode(b'abcd')
print(str_encode)
str_decode = base64.b64decode(str_encode)
print(str_decode)

print(b'abcd')


def safe_base64_decode(s):
    if isinstance(s, str):
        length = len(s)
        if not length % 4 == 0:
            for i in range(4 - length % 4):
                s += '='
        new_str = base64.b64decode(s)
        return new_str
    elif isinstance(s, bytes):
        s += (4 - len(s) % 4) * b'='
        return base64.b64decode(s)


assert b'abcd' == safe_base64_decode(
    b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')

print(2 << 3)

md5 = hashlib.md5()
md5.update('hello workd'.encode('utf-8'))
print(md5.hexdigest())
md5.update('hello world'.encode('utf-8'))
print(md5.hexdigest())
md5_1 = hashlib.md5()
md5_1.update('hello workdhello world'.encode('gbk'))
print(md5_1.hexdigest())

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, password):
    login_md5 = hashlib.md5()
    login_md5.update(password.encode('utf-8'))
    if login_md5.hexdigest() == db[user]:
        return True
    else:
        return False


assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')


natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))


def pi(n):
    series = itertools.count(1, 2)
    series = itertools.takewhile(lambda x: x <= 2 * n - 1, series)
    series = map(lambda x: 4 / x, series)
    series = list(series)
    return reduce(lambda x, y: x + y, [(-1) ** i * series[i] for i in range(len(series))])


print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
