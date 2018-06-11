# -*- coding: utf-8 -*-

from multiprocessing import Process, Pool
import os
import time
import random
import subprocess
import sys


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %0.2f seconds.' % (os.getpid(), end - start))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
    pool = Pool(3)
    for i in range(5):
        pool.apply_async(long_time_task, (i,))
    print('Waiting for all subprocess done...')
    pool.close()
    pool.join()
    print('All subprocess done.')

    print('$ nslookup www.baidu.com')
    r = subprocess.call(['nslookup', 'www.baidu.com'])
    print('Exit code:', r)
