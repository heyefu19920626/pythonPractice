# 函数
- 函数的定义
- 没有return也会有返回值，返回None
- pass占位符的使用,没有会报错
- 参数检查
```python
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x
```
- 可以返回多个值
```python
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, 30)
r = move(100, 100, 60, 30) #返回值其实是一个tuple
```
- 函数参数
    - 必选参数, 位置参数
    - 默认参数
        - 定义时：必选参数在前，默认参数在后
        - 调用时：按顺序传递参数，或者用参数名传递
        - <font color="red">默认参数必须指向不可变对象</font>  
    - 可变参数*, 允许传入0个或任意个参数, 在函数调用时主动组装为一个tuple
    - 关键字参数**, 允许传入0个或任意个参数，在函数调用时自动组装为一个dict,调用者可以传入不受任意限制的参数
    - 命名关键字参数, 以\*隔开，之后的被视为命名关键字参数，如果已经有一个可变参数，则不再需要一个\*了,调用时必须传入参数名, 可以有缺省值，调用时可以不必再传入
    - <font color="red">参数可以自由组合，但顺序必须是：必选，默认，可变，命名， 关键</font>
```python
# Python函数在定义的时候，默认参数就被计算出来了
def add_end(L=[]):
    L.append('END')
    return L

print(add_end())
print(add_end()) # ['END', 'END']

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 可变参数
def calc(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

print(calc(1, 2))
print(calc(1, 3, 5))
nums = [1, 2, 3, 4, 5]
# 用*将列表等转为可变参数
print(calc(*nums))

# 关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'country' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('Tom', 35, city='Beijing', country='China')
extra = {'city': 'Shanghai', 'country': 'China'}
person('Bob', 27, **extra)

def person(name, age, *, city, country):
    print(name, age, city, country)

def person(name, age, *args, city, country):
    print(name, age, args, city, country)

def person(name, age, *, city, country='China'):
    pass
```

- 递归  
    - 理论上，所有的循环都可以写成递归
    - 递归要放置栈帧溢出
    - 尾递归，循环是特殊的尾递归，函数返回时调用自身，return语句不能含有表达式
    - Python解释器没有对尾递归做优化，任何递归都存在栈帧溢出问题
```python
def fact(n):
    if n == 1:
        return 1
    else:
        return  n * fact(n-1)

# 尾递归
def fact(n, product=1):
    if n == 1:
        return product
    return fact(n-1, n * product)
```