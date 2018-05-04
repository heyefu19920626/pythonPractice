# 函数式编程
- [MapReduce](#map_reduce)
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

- map() map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
- reduce() reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
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