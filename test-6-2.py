# coding:utf-8
import Queue
import threading
import urllib2
import re


class Foo(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # get the url from the queue
            url = self.queue.get()
            # 死循环让get不断去取数据，直到阻塞完成，挑出循环
            # download the file
            self.download_url(url)

            # send a signal to the queue that the job is done
            self.queue.task_done()

    def download_url(self, url):
        ''''''
        html = urllib2.urlopen(url).read()
        text_title = re.findall(r'<title>(.*?)</title>', html)
        print text_title


queue = Queue.Queue()
urls = [
    'https://www.yahoo.com/news/',
    'https://www.yahoo.com/news/science/',
    'http://yahoo.com']
for url in urls:
    queue.put(url)

for i in range(3):
    t = Foo(queue)
    t.setDaemon(True)
    t.start()
queue.join()  # 队列阻塞，让每个项都完成
