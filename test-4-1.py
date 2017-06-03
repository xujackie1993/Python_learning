# coding:utf-8
'''
回顾
'''
import threading
import time


def foo():
    start = time.time()
    time.sleep(2)
    end = time.time()
    print threading.currentThread().getName(), '共执行的时间', (end - start)


for i in range(5):
    t = threading.Thread(target=foo)
    t.start()
