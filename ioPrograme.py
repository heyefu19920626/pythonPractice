# -*- coding: utf-8 -*-
from io import StringIO, BytesIO
from objectOriented import Student
import os
import shutil
import pickle
import json


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

b = BytesIO()
b.write('中文'.encode('utf-8'))
print(b.getvalue())


# print(os.environ)
# print(os.environ.get('path'))
print([x for x in os.listdir() if os.path.isfile(
    x) and os.path.splitext(x)[1] == '.py'])
print(os.path.abspath('.'))
print(os.path.join('home', 'heyefu', 'programe'))
# os.mkdir('test')
# os.rmdir('test')
print(os.path.split(os.path.abspath('.')))
os.rename('miku_1.jpg', 'miku_2.jpg')
os.remove('miku_2.jpg')
shutil.copyfile('miku.jpg', 'miku_3.jpg')


# 序列化
d = dict(name='Bob', age=19, sex='M')
print(d)
# pick = pickle.dumps('测试')
pick = pickle.dumps(d)
with open('test.pick', 'wb') as f:
    pickle.dump(pick, f)

with open('test.pick', 'rb') as f:
    print(pickle.load(f))
    # temp = f.read()
    # print(pickle.loads(temp))


with open('test.json', 'w') as f:
    # print(json.dumps(d))
    json.dump(d, f)

with open('test.json') as f:
    js = json.load(f)

print(js)
print(js['age'])


def studentDict(std):
    return {
        'name': std.name,
        'score': std._Student__score,
    }


s = Student('Jeck', 100)
s_json = json.dumps(s, default=studentDict)
print(s_json)


def dictStudent(dic):
    return Student(dic['name'], dic['score'])


s_s = json.loads(s_json, object_hook=dictStudent)
s_s.print_score()
