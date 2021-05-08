# 错误，调试和测试

- [错误处理](#error-handle)
- [调试](#debug)
- [单元测试](#unit-testing)
- [文档测试](#document-test)


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

<div id="unit-testing"></div>

### 单元测试
- unittest
    - 引入Python自带的unittest模块
    - 编写测试类，从unittest.TestCase继承
    - 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
    - 对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()
- 运行单元测试
    - unittest.main()
    - 命令行通过参数 -m unitest
    > python -m unittest **.py
- setUp与tearDown
    - 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行

```python
import unittest
from learn.errorDebugTest import Dict


class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a='aA', b='bB')
        self.assertEqual(d.a, 'aA')
        self.assertEqual(d.b, 'bB')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')


if __name__ == '__main__':
    unittest.main()
```

<div id="document-test"></div>

### 文档测试 doctest
- 当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执行doctest
```python
'''
>>> d = Dict()
>>> d['x'] = 100
>>> d.x
100
'''

if __name__ == '__main__':
    import doctest
    doctest.testmod()
```