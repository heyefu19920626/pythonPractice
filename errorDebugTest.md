# 错误，调试和测试

- [错误处理](#error-handle)
- [调试](#debug)


<div id="error-handle"></div>

### 错误处理
- try expect else finaly
```python
try:
    print('try...')
    10/0
    print('result...')
except Exception as e:
    print('except:', e)
    # raise
else:
    print('else')
finally:
    print('finally')
```

- 记录错误
    - 通过配置，logging可以把错误记录到日志文件里，方便事后排查
- 抛出错误
    - 自定义错误
    - raise语句如果不带参数，就会把当前错误原样抛出
```python
class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


print(foo(2))
```

<div id="debug"></div>

### 调试
- 断言, assert
    - 启动Python解释器时可以用-O参数来关闭assert
    - 关闭后，你可以把所有的assert语句当成pass来看
- logging
    - logging允许指定记录信息的级别，有debug，info，warning，error等几个级别，当指定level=INFO时，logging.debug就不起作用了
    - 通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件
- pdb
    - python -m pdb **.py
    - 输入l查看代码，输入n单步执行代码，输入p 变量名查看变量， 输入q结束调试
- pdb.set_trace()
    - import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
    - 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行
```python
import logging
import pdb


logging.basicConfig(level=logging.INFO)
pdb.set_trace()
```