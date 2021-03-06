# 函数式编程

- [MapReduce](#map_reduce)
- [Filter](#filter)
- [Sorted](#sorted)
- [Rutrun-funcion](#return-function)
- [Anonymity-funcion](#anonymity-function)
- [Decorator](#decorator)
- [Partial-function](#partial-function)
```
  函数式编程就是一种抽象程度很高的编程范式，
  纯粹的函数式编程语言编写的函数没有变量，
  因此，任意一个函数，只要输入是确定的，输出就是确定的，
  这种纯函数我们称之为没有副作用。
  而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，
  因此，这种函数是有副作用的。  
  函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
```
- 变量可以指向函数
> f = abs  
> f(-10)
- 函数名也是变量， 函数名是指向函数的变量
- 高阶函数(High-order function)
    - 编写高阶函数，就是让函数的参数可以接收别的函数
```python
def add(x, y, f):
    return f(x) + f(y)
```
<div id="map_reduce"></div>

- map(): map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
- reduce(): reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
> reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```python
def normalize(name):
    return name[0].upper() + name[1:].lower()
print(list(map(normalize, ['adam', 'LISA', 'barT'])))

from functools import reduce
def prod(L):
    return reduce(lambda x, y: x * y, L)
print(prod([3, 5, 7, 9]))

def str2float(s):
    """ 将字符串转化为整数或小数 """
    def getNum(key):
        nums = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return nums[key]

    def getInt(x, y):
        return x * 10 + y

    def getFloat(x, y):
        return 0.1 * x + 0.01 * y

    def getPower(x):
        return reduce(lambda x, y: x * y, [10 for i in range(x)])

    index = 0
    if '.' in s:
        index = len(s) - s.rindex('.') - 1
        s = s.replace('.', '')

    if index:
        return reduce(getInt, map(getNum, s)) / getPower(index)

    return reduce(lambda x, y: x * 10 + y, map(getNum, s))

str2float('245.698') # 245.698

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)
```

<div id="filter"></div>

- filter():接收一个函数和一个序列,filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
    - filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素
```python
def old_iter():
    """ 构造一个从3开始的奇数序列 """
    n = 1
    while True:
        n = n + 2
        yield n


def not_prime(n):
    """ 筛选序列 """
    return lambda x: x % n > 0


def primes():
    """ 生成器， 返回素数 """
    yield 2
    it = old_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_prime(n), it)


for n in primes():
    if n < 1000:
        print(n)
    else:
        break


def is_palindrome(n):
    return int(str(n)[::-1]) == n # 切片操作的最后一个参数可以看做步长或者偏移量


# 筛选回数
print(list(filter(is_palindrome, range(1000))))
```

<div id="sorted"></div>

- sorted是一个高阶函数，它还可以接收一个key函数来实现自定义的排序.
    - key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
    - 用sorted()排序的关键在于实现一个映射函数
```python
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


def by_score(t):
    return t[1]


print(L)
print(sorted(L, key=by_name))
print(sorted(L, key=by_score))
```

<div id="return-function"></div>
- 返回函数
    - 内部函数sum可以引用外部函数lazy_sum的参数和局部变量
    - 每次调用都会返回一个新的函数，即使传入相同的参数
    - 返回的函数并没有立刻执行，而是直到调用了f()才执行
```python
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum


f = lazy_sum(1, 2, 3, 4, 5)
print(f)
print(f())
```
- 闭包
    - <font color="red">返回函数不要引用任何循环变量，或者后续会发生变化的变量</font>
    - 内部函数只有读闭包的权限，没有写闭包的权限。可以用nonlocal来解决
    - nonlocal global
```python
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3()) # 9, 9, 9

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

def createCounter():
    i = 0

    def count():
        nonlocal i
        i += 1
        return i
    return count


countA = createCounter()
print(countA(), countA())
```

<div id="anonymity-function"></div>

- 匿名函数
    + lambda
```python
L = list(filter(lambda x: x % 2 == 0, range(0, 20)))
```

<div id="decorator"></div>

- 装饰器
    - 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
```python
def log(func):
    def wapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wapper


@log
def now():
    print('2018-05-07')


now1 = log(now)  # log(log(now)) -> log(wapper)
now1()

now()
```
    - 带参数的装饰器
```python
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wapper(*args, **kw):
            print('call %s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wapper
    return decorator


@log('execute')
def now():
    print('2018-05-07')


now1 = log('execute 1')(now)  # log(log(now)) -> log(wapper)
now1()

print(now.__name__)
now()

# 打印函数执行时间
def metric(fn):
    @functools.wraps(fn)
    def wapper(*args, **kw):
        start = time.time()
        result = fn(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end - start))
        return result

    return wapper


@metric
def fast(x, y):
    time.sleep(0.002)
    return x + y

f = fast(11, 22)
```

<div id="partial-function"></div>

- 偏函数
```python
def int2(x, base=2):
    return int(x, base)


print(int2('100001'))

int3 = functools.partial(int, base=2)
print(int3('11111'))

max2 = functools.partial(max, 10)
print(max2(2, 6, 7))
```