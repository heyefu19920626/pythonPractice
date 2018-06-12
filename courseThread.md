# 进程和线程

- [多进程](#multiprocess)
- [多线程](#multithread)

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
    + Popen()类
    + call()方法
    + communicate()子进程的输入
```python
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code:', p.returncode)
```

- 进程间通信
- 通过Queue, Pipes等方式实现
```python
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['a', 'b', 'c']:
        print('Put %s to  queue...' % value)
        q.put(value)
        time.sleep(random.random() * 3)

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

# 进程间通信
q = Queue()
pw = Process(target=write, args=(q,))
pr = Process(target=read, args=(q,))

pw.start()
pr.start()
pw.join()
# pr 进程是死循环，无法等待期结束，只能强行终止
pr.terminate()
```

<div id="multithread"></div>

### 多线程
- 进程是由若干线程组成的，一个进程至少有一个线程
- \_thread与threading模块
- 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行