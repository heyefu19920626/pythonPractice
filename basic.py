
# Python 字符串编码
# Python3 默认Unicode编码
print("中文")
print("\u4e2d\u6587")

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

print('Hello, {0}, 成绩提升了{1}'.format('小明', 17))