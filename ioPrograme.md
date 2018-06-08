# IO编程

- [文件读写](#file-read-write)

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
