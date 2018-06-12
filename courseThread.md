# 进程和线程

- [多进程](#multiprocess)
- [多线程](#multithread)
- [ThreadLocal](#threadlocal)

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
```python
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        print('thread %s >>> %d' % (threading.current_thread().name, n))
        time.sleep(1)
        n += 1
    print('thread %s is ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='子线程')
t.start()
t.join()
print('thread %s is ended.' % threading.current_thread().name)
```

#### Lock
- 多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响
- 多线程中，所有变量都由所有线程共享
- 当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止
- 获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程
```python
balance = 0
lock = threading.Lock()
def change_i(n):
    global balance
    balance += n
    balance -= n


def run_thread(n):
    for i in range(10000000):
        # 获取锁
        lock.acquire()
        try:
            change_i(n)
        finally:
            # 释放锁
            lock.release()

# Lock
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
```

- Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核

<div id="threadlocal"></div>

### ThreadLocal