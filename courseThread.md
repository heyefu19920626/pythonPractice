# 进程和线程

- [多进程](#multiprocess)

- 多任务实现的三种方式
    - 多进程
    - 多线程
    - 多进程 + 多线程
- 线程是最小的执行单元，而进程由至少一个线程组成

<div id="multiprocess"></div>

### 多进程
- unix/linux
    - fork()
- getpid(), getppid()
- multiprocessing模块
- join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
```python
from multiprocessing import Process
import os


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
```
- 进程池
- Pool
    - 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
```python
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %0.2f seconds.' % (os.getpid(), end - start))

pool = Pool(3)
for i in range(5):
    pool.apply_async(long_time_task, (i,))
print('Waiting for all subprocess done...')
pool.close()
pool.join()
print('All subprocess done.')
```

- 子进程
- subprocess模块