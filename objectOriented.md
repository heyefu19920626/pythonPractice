# 面向对象编程(Object Oriented Programming)

- [Class-Instance](#class-instance)
- [Access-Restriction](#access-restriction)
- [Polymorphism](#polymorphism)
- [GetObjectInfomation](#get-object-infor)
- [ClassAndInstanceProperty](#class-instance-property)
<div id="class-instance"></div>

### 类和实例
- OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数 
- 面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行
- 面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递
- 给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法（Method）
- 数据封装、继承和多态是面向对象的三大特点
- 面向对象最重要的概念就是类（Class）和实例（Instance）
- 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数
- 类的__init__构造函数
```python
# 括号内object表示继承的类，如果没有，则写object
class Student(object):
    """docstring for Student"""

    #  构造方法
    def __init__(self, name, score=90):
        self.name, self.score = name, score

    def print_score(self):
        print('%s的成绩是:%s' % (self.name, self.score))


tom = Student('tom')
print(tom)
tom.print_score()
```
- Python允许对实例变量绑定任何数据

<div id="access-restriction"></div>

### 访问限制
- 让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
- 实际上还是可以访问,通过_Student__score,即_类名__变量名,因为Python解释器对外把__name变量改成了_Student__name,不同的Python解释器有可能改成不同改的变量名
- 可以为外部留出get，set接口
```python
class Student(object):
    """docstring for Student"""

    #  构造方法
    def __init__(self, name, score=90):
        self.name, self.__score = name, score

    def print_score(self):
        print('%s的成绩是:%s' % (self.name, self.__score))


tom = Student('tom')
print(tom)
tom.print_score()
print(tom._Student__score)
```

<div id="polymorphism"></div>

### 继承和多态
- 定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）
- 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写
- 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的
```python
class Animal(object):

    def run(self):
        print('Animal is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run(animal):
    if isinstance(animal, Animal):
        animal.run()
    else:
        print('请传入Animal')


cat = Cat()
run(cat)


class Dog(Animal):

    def run(self):
        print('Dog is running...')


run(Dog())
run(Student('Bob'))
```

<div id="get-object-infor"></div>

### 获取对象信息

- type
    - type()函数返回对应的Class类型
    - 在if语句中判断,可以使用types模块中定义的常量
- isinstance
    - isinstance()就可以告诉我们，一个对象是否是某种类型
- dir
    - dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
    - 类似__xxx__的属性和方法在Python中都是有特殊用途的,比如__len__方法返回长度
- 操作对象的状态
    - 使用getattr(), setattr(),以及hasattr()直接操作对象状态
    - 只有在不知道对象信息的时候，我们才会去获取对象信息
```python
# type
print(type(123))
print(types.FunctionType == type(run))
# isinstance
print(isinstance(cat, Animal))
print(isinstance(123, str))
# dir
print(dir('abc'))
# attr
print(hasattr(cat, 'run'))
print(hasattr(cat, 'runs'))
try:
    print(cat.name)
except Exception as e:
    print(e)
setattr(cat, 'name', 'Tome')
print(cat.name)
fn = getattr(cat, 'run')
fn()


def readImage(fp):
    # 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，
    # 如果存在，则该对象是一个流，如果不存在，则无法读取
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
```

<div id="class-instance-property"></div>

### 实例属性和类属性
- 给实例绑定属性的方法是通过实例变量,或者通过self变量，一般在__init__函数中
- 类本身需要绑定一个属性可以直接在class中定义,这个属性桂类所有，所有实例都可以访问
- 相同名称的实例属性将屏蔽掉类属性，当删除实例属性后，再使用相同的名称，访问到的将是类属性
```python
class Student(object):
    """docstring for Student"""
    email = 'test@email'

    #  构造方法
    def __init__(self, name, score=90):
        # self.name, self.email, self.__score = name, 'test@email', score
        self.name, self.__score = name, score

    def print_score(self):
        print('%s的成绩是:%s, 邮箱是：%s' % (self.name, self.__score, self.email))


tom = Student('tom')
print(tom)
print(tom.email)
Student.email = 'modify@email'
tom.print_score()
print(tom._Student__score)
bob = Student('Bob')
bob.print_score()
print(Student.email)
print(bob.email)
```