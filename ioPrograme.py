# -*- coding: utf-8 -*-



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