# coding:utf-8
'''
queue  队列
'''
import Queue

q = Queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print q.get()
