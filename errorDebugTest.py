# -*- coding: utf-8 -*-

from functools import reduce
import logging
import pdb


logging.basicConfig(level=logging.INFO)


try:
    print('try...')
    10/0
    print('result...')
except Exception as e:
    pass
    # logging.exception(e)
    # raise
else:
    print('else')
finally:
    print('finally')


print('End')


# class FooError(ValueError):
#     pass


# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n


# print(foo(2))


def str2num(s):
    try:
        return int(s)
    except:
        return float(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


# pdb.set_trace()
main()


s = '0'
n = int(s)
logging.info('m = %d' % n)
print(10 / 3)
print('end')


class Dict(dict):
    '''
    >>> d = Dict()
    >>> d['x'] = 100
    >>> d.x
    100
    '''
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except Exception as e:
            raise AttributeError

    def __setattr__(self, key, value):
        self[key] = value

d = Dict(a='1', b='2')
print(d)
print(d.a)

d_d = {'c': '3', 'd': '4'}
print(d_d)
print(d_d['c'])
d_d_d = dict({'e': '5', 'f': '6'})


if __name__ == '__main__':
    import doctest
    doctest.testmod()
