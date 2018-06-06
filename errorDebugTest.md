# 错误，调试和测试

- [错误处理](#error-handle)


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