# coding:utf-8
import threading
import time


class Foo(threading.Thread):
    def run(self):
        print threading.currentThread().getName(), '开始\n'
        print threading.currentThread().getName(), 'end\n'


def foo():
    print threading.currentThread().getName(), '开始\n'
    time.sleep(2)
    print threading.currentThread().getName(), 'end\n'


t = Foo()
d = threading.Thread(target=foo)
t.start()
d.setDaemon(True)  # 设置守护进程
d.start()
d.join()  # 阻塞  代码执行完才能结束
