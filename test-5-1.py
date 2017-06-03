# coding:utf-8

import threading

num = 0


def foo():
    global num
    num += 1
    print num, '\n'


for i in xrange(5):
    t = threading.Thread(target=foo)
    lock = threading.Lock()
    lock.acquire()  # 获取GIL锁，防止线程混乱
    t.start()
    lock.release()  # 释放锁
