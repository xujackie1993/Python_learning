# coding:utf-8

import threading
import time


class Foo(threading.Thread):
    def run(self):
        start = time.time()
        time.sleep(2)
        end = time.time()
        print threading.currentThread().getName(), '共执行的时间', (end - start)


for i in range(5):

    t = Foo()
    t.start()
