# IO编程

- [文件读写](#file-read-write)
- [StringIO与BytesIO](#stringIO-bytesIO)
- [操作文件和目录](#file-diretory)
- [序列化](#serialization)

<div id="file-read-write"></div>

### 文件读写
- 在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘
- 读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）
```python
with open('test_module.py') as f:
    # for line in f:
    #     print(line.strip())
    # line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()

with open('test.py') as f:
    with open('test_w.py', 'w') as w:
        w.write(f.read())

with open('miku.jpg', 'rb') as f:
    with open('miku_1.jpg', 'wb') as w:
        w.write(f.read())
```

- file-like Object
    - 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Objec
    - file-like Object不要求从特定类继承，只要写个read()方法就行


<div id="stringIO-bytesIO"></div>

### StringIO与BytesIO
- 用StringIO()去初始化的时候，其指针是指向0的位置；而如果是用write的方法的时候，其指针则是会移动到后面的
- tell 方法获取当前文件读取指针的位置
- seek 方法，用于移动文件读写指针到指定位置,有两个参数，第一个offset: 偏移量，需要向前或向后的字节数，正为向后，负为向前；第二个whence: 可选值，默认为0，表示文件开头，1表示相对于当前的位置，2表示文件末尾
-  用seek方法时，需注意，如果你打开的文件没有用'b'的方式打开，则offset无法使用负值
```python
from io import StringIO, BytesIO

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
```

<div id="file-diretory"></div>

### 操作文件和目录
- 环境变量: environ
- 操作文件和目录
    - os与os.path模块
    - shutil模块
```python
# print(os.environ)
# print(os.environ.get('path'))
print([x for x in os.listdir() if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
print(os.path.abspath('.'))
print(os.path.join('home', 'heyefu', 'programe'))
# os.mkdir('test')
# os.rmdir('test')
print(os.path.split(os.path.abspath('.')))
os.rename('miku_1.jpg', 'miku_2.jpg')
os.remove('miku_2.jpg')
shutil.copyfile('miku.jpg', 'miku_3.jpg')
```

<div id="serialization"></div>

### 序列化
- 把变量从内存中变成可存储或传输的过程称之为序列化
- 反序列化
- pickle模块
- json模块
```python
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
```