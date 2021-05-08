from collections import Iterable


print(isinstance('abc', Iterable))
print(isinstance(2, Iterable))

l = [x for x in range(1, 100) if x % 2 == 0]
print(l)

l = [m + n for m in 'ABC' for n in 'XYZ']
print(l)

l = list(range(1, 10))
print(l)

g = (x * x for x in range(1, 10))
print(g)
print(next(g))

for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


for f in fib(10):
    print(f)

g = fib(10)
while True:
    try:
        x = next(g)
        print('g: ', x)
    except StopIteration as e:
        print('Generator return value: ' + e.value)
        break
