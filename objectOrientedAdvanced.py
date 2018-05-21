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


def set_score(self, score):
    self.score = score


Student.sex = 'Man'
Student.set_score = set_score

s1 = Student()
s1.set_score(95)
print(s1.score)


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
