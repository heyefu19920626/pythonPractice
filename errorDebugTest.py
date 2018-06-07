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


pdb.set_trace()
main()


s = '0'
n = int(s)
logging.info('m = %d' % n)
print(10 / n)
print('end')
