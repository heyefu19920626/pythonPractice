import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x


print(my_abs(-5))
print(my_abs(3))
# print(my_abs('a'))


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, 30)
print(x, y)
print(move(100, 100, 60, 60))


def add_end(L=[]):
    L.append('END')
    return L


print(add_end())
print(add_end())


def calc(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum


print(calc(1, 2))
print(calc(1, 3, 5))
nums = [1, 2, 3, 4, 5]
print(calc(*nums))


# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)

def person(name, age, *, city, country):
    print(name, age, city, country)


# person('Tom', 35, city='Beijing', country='China', job='Student')
extra = {'city': 'Shanghai', 'country': 'China'}
person('Bob', 27, **extra)


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


print(fact(100))


def fact_iter(n, product):
    if n == 1:
        return product
    return fact_iter(n-1, n * product)


print(fact_iter(1000, 1))
