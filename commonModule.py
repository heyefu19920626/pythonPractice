import datetime
from datetime import timedelta
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter
import base64
import re


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
