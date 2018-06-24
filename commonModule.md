# 常用内建模块

- [datetime](#datetime)
- [collections](#collections)
- [base64](#base64)
- [struct](#struct)
- [hashlib](#hashlib)
- [hmac](#hmac)
- [itertools](#itertools)

<div id="datetime"></div>

### datetime
- 存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关
```python
import datetime
from datetime import timedelta

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
```

<div id="collections"></div>

### collections
- 一个集合模块
- namedtuple
    - namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
- deque
    - deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
- defaultdict
    - 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
- OrderRedDict
    - OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
- Counter
    - Counter是一个简单的计数器，例如，统计字符出现的个数
```python
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
```

<div id="base64"></div>

### base64

- base64原理
    - 准备一个包含64个字符的数组
    - 对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4组，每组正好6个bit
    - 得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串
    - 如果要编码的二进制数据不是3的倍数，用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉
```python
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
```

<div id="struct"></div>

### struct
- 用来解决bytes和其他二进制数据类型的转换

<div id="hashlib"></div>

### hashlib
- 摘要算法
    - 摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）
    - 防篡改
- md5,sha1,sha256,sha512
```python
md5 = hashlib.md5()
md5.update('hello workd'.encode('utf-8'))
print(md5.hexdigest())
md5.update('hello world'.encode('utf-8'))
print(md5.hexdigest())
md5_1 = hashlib.md5()
md5_1.update('hello workdhello world'.encode('gbk'))
print(md5_1.hexdigest())
```

<div id="hmac"></div>

### hmac
- Hmac算法：Keyed-Hashing for Message Authentication
    - 通过一个标准算法，在计算哈希的过程中，把key混入计算过程中
    - hamc实现带key的哈希


<div id="itertools"></div>

### itertools
- itertools提供了非常有用的用于操作迭代对象的函数
- count()会创建一个无限的迭代器
- cycle()会把传入的一个序列无限重复下去
- repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
- 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素
- 可以通过takewhile()等函数根据条件判断来截取出一个有限的序列
- chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
- groupby()把迭代器中相邻的重复元素挑出来放在一起
- itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算
```python
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
```