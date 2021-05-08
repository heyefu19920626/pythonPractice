# 模块
- 模块(module)
- 包(package)
    - 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的
    - __init__.py可以是空文件，也可以有Python代码
    - __init__.py本身就是一个模块，而它的模块名就是包名
- 公开与私有
    - 正常的函数和变量名是公开的（public），可以被直接引用
    - 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途,自己的变量一般不要用这种变量名
    - 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用
    - 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public
```python
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
```

- 模块搜索路径
    - 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中
    > import sys  
    > sys.path