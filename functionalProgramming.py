from functools import reduce

f = abs
print(f)
print(f(-10))


def normalize(name):
    return name[0].upper() + name[1:].lower()


print(list(map(normalize, ['adam', 'LISA', 'barT'])))


def prod(L):
    return reduce(lambda x, y: x * y, L)


print(prod([3, 5, 7, 9]))


def str2float(s):
    def getNum(key):
        nums = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return nums[key]

    def getInt(x, y):
        return x * 10 + y

    def getFloat(x, y):
        return 0.1 * x + 0.01 * y

    def getPower(x):
        return reduce(lambda x, y: x * y, [10 for i in range(x)])

    index = 0
    if '.' in s:
        index = len(s) - s.rindex('.') - 1
        s = s.replace('.', '')

    if index:
        return reduce(getInt, map(getNum, s)) / getPower(index)

    return reduce(lambda x, y: x * 10 + y, map(getNum, s))


print(str2float('4569') + 5)

print(reduce(lambda x, y: x * 10 + y, [2, 4, 4])/1000)

# str2float('12.56')

print(reduce(lambda x, y: x * y, [10 for i in range(5)]))

print(str2float('456.2587') + 5)

print(str2float('.1234'))


def old_iter():
    """ 构造一个从3开始的奇数序列 """
    n = 1
    while True:
        n = n + 2
        yield n


def not_prime(n):
    """ 筛选序列 """
    return lambda x: x % n > 0


def primes():
    """ 生成器， 返回素数 """
    yield 2
    it = old_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_prime(n), it)


# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break


def is_palindrome(n):
    return int(str(n)[::-1]) == n


# 筛选回数
print(list(filter(is_palindrome, range(1000))))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# sorted
def by_name(t):
    return t[0]


def by_score(t):
    return t[1]


print(L)
print(sorted(L, key=by_name))
print(sorted(L, key=by_score))


# return function
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum


f = lazy_sum(1, 2, 3, 4, 5)
print(f)
print(f())


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


def createCounter():
    i = 0

    def count():
        nonlocal i
        i += 1
        return i
    return count


countA = createCounter()
print(countA(), countA())
countB = createCounter()
print(countB(), countB())