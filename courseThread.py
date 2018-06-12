# -*- coding: utf-8 -*-

from multiprocessing import Process, Pool, Queue
import os
import time
import random
import subprocess
import sys
import threading


balance = 0
lock = threading.Lock()


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %0.2f seconds.' % (os.getpid(), end - start))


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


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        print('thread %s >>> %d' % (threading.current_thread().name, n))
        time.sleep(1)
        n += 1
    print('thread %s is ended.' % threading.current_thread().name)


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


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

    # 进程池
    pool = Pool(3)
    for i in range(5):
        pool.apply_async(long_time_task, (i,))
    print('Waiting for all subprocess done...')
    pool.close()
    pool.join()
    print('All subprocess done.')

    # 子进程

    print('$ nslookup www.baidu.com')
    r = subprocess.call(['nslookup', 'www.baidu.com'])
    print('Exit code:', r)

    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('gbk'))
    print('Exit code:', p.returncode)

    # 进程间通信
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()
    pw.join()
    # pr 进程是死循环，无法等待期结束，只能强行终止
    pr.terminate()

    # 多线程
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='子线程')
    t.start()
    t.join()
    print('thread %s is ended.' % threading.current_thread().name)

    # Lock
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
