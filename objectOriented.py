#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

# 括号内object表示继承的类，如果没有，则写object


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
