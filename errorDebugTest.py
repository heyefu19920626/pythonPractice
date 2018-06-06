# -*- coding: utf-8 -*-

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
