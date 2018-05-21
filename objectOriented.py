#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import types

# 括号内object表示继承的类，如果没有，则写object


class Student(object):
    """docstring for Student"""
    # email = 'test@email.com'

    #  构造方法
    def __init__(self, name, score=90):
        # self.name, self.email, self.__score = name, 'test@email', score
        self.name, self.__score = name, score

    def print_score(self):
        print('%s的成绩是:%s, 邮箱是：%s' % (self.name, self.__score, self.email))


tom = Student('tom')
print(tom)
Student.email = 'modify@email'
print(tom.email)
tom.print_score()
print(tom._Student__score)
bob = Student('Bob')
bob.print_score()
print(Student.email)
print(bob.email)


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

print(type(cat))
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
