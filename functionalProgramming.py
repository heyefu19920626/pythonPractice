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
