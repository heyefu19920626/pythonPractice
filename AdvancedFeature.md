# 高级特性
- Slice切片
    - L[0:3] 不包括3
    - L[:]复制一个列表
    - tuple也可以切片，之后还是tuple
    - str也可以切片
- Iteration迭代
    - for in
    - 列表，字典，字符串等都可以迭代
    - 判断是否可迭代：通过collections模块的Iterable
    - 下标循环：enumerate函数可以把一个列表变为索引-元素对
```python
for v in dic.values():
    pass
# 同时迭代key， value
for k, v in dict.items():
    pass
# 判断是否可迭代
from collections import Iterable

isinstance('abc', Iterable)

for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)
```
- 列表生成式
> l = list(range(1,100))  
> l = [x for x in range(1,100) if x % 2 == 0]  
> l = [m + n for m in 'ABC' for n in 'XYZ']  
> l = [k + '=' + v for k, v in d.itens()]
- generator生成器
    - generator中存储的是表达式，只有需要的时候才生成
    - 将列表生成式的中括号[]改为()
    > g = (x * x for x in range(1, 10))
    - next访问,获取下一个值,没有值后会报StopIteration错误
    > next(g)
    - for in 访问
    - yield关键字将函数变为generator
```python
for n in g:
    print(n)

a, b = b, a+b
# 相当于
t = (b, a + b)
a = t[0]
b = t[1]

# 函数式生成器
''' generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行 '''
def fib(max):
    n, a, b = 0, 0 , 1
    while n < max:
        yield b
        # print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
for f in fib(10):
    print(f)

''' 想拿到return返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中 '''
g = fib(10)
while True:
    try:
        x = next(g)
        print('g: ', x)
    except StopIteration as e:
        print('Generator return value: ' + e.value)
        break
```
- Iterator迭代器
    - 凡是可作用于for循环，都是Iterable
    - 可以被next()函数调用，并返回下一个值,都是Iterator
    - 生成器都是Iterator对象，list，dict等是Iterable但不是Iterator
    - Iterator是惰性的，只有在需要返回下一个数据时它才计算
    - Iterator可以表示一个无限大的数据流，但list等不行