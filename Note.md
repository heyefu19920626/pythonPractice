# Python基础

### 数据类型和变量
- Python的数据类型
    1. 浮点型
    2. 整型
    3. 字符串
    4. 布尔
    5. None
> python的整数没有大小限制
> python的浮点数也没有大小限制，但是超出一定范围就显示为inf（无限大）

- 变量与常量
> 常量实际上仍是变量

- / 与 //
> 9 / 3 = 3.0
> 9 // 3 = 3 地板

### 字符串和编码
- Python3默认编码为Unicode
- Python的字符串类型是str，传输要转为bytes，Ascii可以用b'ABC'形式直接转为byte
- str可以用encode()方法编码为指定的bytes
- bytes转为str可以用decode()
- 声明解释器和编码方式并保存为对应编码一般能够保证程序中写死的输出不乱码
```
#!/usr/bin/python3
# -*- encoding: utf-8 -*-
```
- 格式化字符串
> "Hello %s" % "word"  
> 'Hi, %s, you have $ %d' % ('Niko', 10000)  

| 占位符 | 替换内容 |
|:--:|:--:|
%d | 整数
%f | 浮点数
%s | 字符串
%x | 十六制整数
%% | %
- format()方法也可以格式化字符串
> 'Hello, {0}, 成绩提升了{1}'.format('小明', 17)

### list列表
- 访问
```
    classmates = ['1', '2', 'list',[2, 3, 4, 'list']]
    print(classmates[-1][-1])
```
- 列表操作:append(), pop(), insert()
```
    classmates.append(['append', '3']);
    classmates.append(5)
    classmates.pop()
    classmates.pop(1)
```