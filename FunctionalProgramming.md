# 函数式编程
## 高阶函数
- [MapReduce](#map_reduce)
- [Filter](#filter)
- [Sorted](#sorted)
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