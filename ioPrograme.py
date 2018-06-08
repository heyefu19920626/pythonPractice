# -*- coding: utf-8 -*-
from io import StringIO, BytesIO



with open('test_module.py') as f:
    for line in f:
        print(line.strip())
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()

with open('test.py') as f:
    with open('test_w.py', 'w') as w:
        w.write(f.read())

with open('miku.jpg', 'rb') as f:
    with open('miku_1.jpg', 'wb') as w:
        w.write(f.read())


# StringIO
s = StringIO('12345')
print(s.tell())
print(s.getvalue())
s.write('abc')
print(s.getvalue())
print(s.tell())
s.write('defg')
print(s.getvalue())
s.seek(0, 0)
print(s.read())

b = BytesIO();
b.write('中文'.encode('utf-8'))
print(b.getvalue())