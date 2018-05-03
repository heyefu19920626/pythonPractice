
# Python 字符串编码
# Python3 默认Unicode编码
print("中文")
print("\u4e2d\u6587")

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

print('Hello, {0}, 成绩提升了{1}'.format('小明', 17))


classmates = ['1', '2', 'list', [2, 3, 4, 'list']]
print(classmates[-1][-1])

classmates.append(['append', '3'])
classmates.append(5)
print(classmates)
classmates.pop()
classmates.pop(1)
classmates.insert(0, 'insert')
print(classmates)

t = (1, 2, [3, 4])
t[-1][-1] = 5
print(t)

d = {'a': 1, 'b': 2}
print(d)
print('a' in d)