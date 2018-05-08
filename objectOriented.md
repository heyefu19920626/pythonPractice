# 面向对象编程(Object Oriented Programming)

- [Class-Instance](#class-instance)
- [Access-Restriction](#access-restriction)
- [Polymorphism](#polymorphism)
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