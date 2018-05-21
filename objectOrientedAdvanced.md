# 面向对象高级编程

- [__slots__](#slots)
- [@property](#@property)

<div id="slots"></div>

### 使用__slots__限制实例的属性
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