# 面向对象高级编程

- [\_\_slots\_\_](#slots)
- [@property](#@property)
- [多重继承](#multiple-inherit)
- [定制类](#custom-class)
- [使用枚举类](#eunm-class)
- [使用元类](#meta-calss)

<div id="slots"></div>

### 使用\_\_slots\_\_限制实例的属性
- 给实例绑定属性和方法
```python
from types import MethodType


class Student(object):
    pass


def set_age(self, age):
    self.age = age


s = Student()
s.name = 'Bob'
print(s.name)
# 给实例绑定一个方法
s.set_age = MethodType(set_age, s)
s.set_age(18)
print(s.age)
```
- 给类绑定属性和方法
```python
def set_score(self, score):
    self.score = score


Student.sex = 'Man'
Student.set_score = set_score

s1 = Student()
s1.set_score(95)
print(s1.score)
```
- __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
- 在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
```python
class Teacher(object):
    __slots__ = ('name', 'sex', 'age', 'set_age')


t = Teacher()
t.age = 27
print(t.age)
Teacher.sex = 'Women'
print(t.sex)
# t.address = 'Beijing'
Teacher.set_age = set_age
t.set_age(25)
print(t.age)
```

<div id="@property"></div>

### @property装饰器负责把一个方法变成属性调用的
- @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查
```python
class Animal(object):

    def __init__(self):
        self.__name = 'Animal'

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type


dog = Animal()
dog.type = 'dog'
print(dog.type)
```

<div id="multiple-inherit"></div>

### 多重继承
- Mixln, MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系
- python继承顺序遵循C3算法，只要在一个地方找到了所需的内容，就不再继续查找
- 拓扑排序(Topological Sorting) 是一个 有向无环图(DAG,Directed Acyclic Graph) 的所有顶点的线性序列,且该序列必须满足下面两个条件:
    + 每个顶点出现且只出现一次
    + 若存在一条从顶点A到顶点B的路径，那么在序列中顶点A出现在顶点B的前面
- [Python多重继承之拓扑排序](https://kevinguo.me/2018/01/19/python-topological-sorting/)

<div id="custom-class"></div>

### 定制类
- __\_\_str\_\___
```python
print(dog)


def get_str(self):
    return '这是Animal类'


Animal.__str__ = get_str
print(dog)
```
- __\_\_repr\_\___
    - __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
```python
__repr__ = __str__
```
- __\_\_iter\_\___
    - 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
```python
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)
```
- __\_\_getitem\_\___
    + 要表现得像list那样按照下标取出元素，需要实现\_\_getitem\_\_()
    + 如果要支持切片操作，需要自己定义
```python
def __getitem__(self, n):
    a, b = 1, 1
    for x in range(n):
        a, b = b, a + b
    return a
f = Fib()
print(f[6])

# 支持slice,不支持step
def __getitem__(self, n):
    if isinstance(n, int):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
    if isinstance(n, slice):
        start = n.start
        stop = n.stop
        if start is None:
            start = 0
        a, b = 1, 1
        L = []
        for x in range(stop):
            if x >= start:
                L.append(a)
            a, b = b, a + b
        return L
```
- __\_\_getattr\_\___
    - 动态返回一个属性
    - 只有在没有找到属性的情况下，才调用\_\_getattr\_\_
```python
def get_attr(self, attr):
    if attr == 'country':
        return lambda: 'China'
    return 'None'

Student.__getattr__ = get_attr
print(s.country())
```
- __\_\_call\_\___
    - 任何类，只需要定义一个\_\_call\_\_()方法，就可以直接对实例进行调用
    - 通过callable()函数，判断一个对象是否可调用
```python
def call(self, address='Beijing'):
    print('My name is %s, I live in %s' % (self.name, address))


Student.__call__ = call
s()
print(callable(Student()))
print(callable([1,2,3,4,5]))
```
- 还有更多的可定制方法，[Python官方文档](https://docs.python.org/3/reference/datamodel.html#special-method-names)

<div id="eunm-class"></div>

### 使用枚举类
- Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较
- 自定义类,使用Enum派生
- @unique装饰器帮助检查保证没有重复值
- 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量
```python
from enmu import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Web = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Month(2))
print(Weekday.Mon)
print(Weekday['Fri'])
print(Weekday(3).value)
```

<div id="meta-calss"></div>

### 使用元类
- 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
- type()函数可以查看一个类型或变量的类型
- type()函数既可以返回一个对象的类型，又可以创建出新的类型
- 要创建一个class对象，type()函数依次传入3个参数
    - class的名称
    - 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法
    - class的方法名称与函数绑定