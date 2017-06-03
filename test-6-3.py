# coding:utf-8
'''生产者、消费者'''
import Queue
import threading
import urllib2
import re


class Foo(threading.Thread):
    def __init__(self, queue, out_queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.out_queue = out_queue

    def run(self):
        while True:
            # get the url from the queue
            url = self.queue.get()
            # 死循环让get不断去取数据，直到阻塞完成，挑出循环
            # out_queue.put(self.download_url(url))
            for item in self.download_url(url):
                out_queue.put(item)
            self.queue.task_done()

    def download_url(self, url):
        ''''''
        html = urllib2.urlopen(url).read()
        url_href = re.findall(r'href=\"(.+?)\"', html)  # 取每个网页的超级链接
        return url_href


class Consumer(threading.Thread):
    '''Threaded Url Grab'''

    def __init__(self, out_queue):
        threading.Thread.__init__(self)
        self.out_queue = out_queue

    def run(self):
        while True:
           # grabs host from queue
            url_list = self.out_queue.get()
            try:
                html = urllib2.urlopen(url_list).read()
                text_title = re.findall(r'<title>(.*?)</title>', html)
                print text_title
            except BaseException:
                pass
            self.out_queue.task_done


queue = Queue.Queue()
out_queue = Queue.Queue()
urls = [
    'https://yahoo.com/',
    'https://www.yahoo.com/news/weather/'
]
for url in urls:
    queue.put(url)

for i in range(2):
    t = Foo(queue, out_queue)
    t.setDaemon(True)
    t.start()

for i in range(5):
    t = Consumer(out_queue)
    t.setDaemon(True)
    t.start()

queue.join()  # 队列阻塞，让每个项都完成
out_queue.join()
