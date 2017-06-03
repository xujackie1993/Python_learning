# coding:utf-8
import threading
import urllib2


class FetchUrls(threading.Thread):
    '''
    Thread checking url
    '''

    def __init__(self, urls, output):
        threading.Thread.__init__(self)
        self.urls = urls
        self.output = output

    def run(self):
        '''
        Thread run method.Check urls one by one
        '''
        while self.urls:
            url = self.urls.pop()
            req = urllib2.Request(url)
            try:
                d = urllib2.urlopen(req)
            except urllib2.URLError as e:
                print 'URL %s failed:%s' % (url, e.reason)
            self.output.write(d.read())
            print 'wirte done by %s' % self.name
            print 'URL %s fetched by %s' % (url, self.name)


def main():
    urls1 = ['https://www.baidu.com/', 'http://www.qq.com/']
    urls2 = ['http://www.163.com/', 'http://www.sohu.com/']
    f = open('output.txt', 'w+')
    t1 = FetchUrls(urls1, f)
    t2 = FetchUrls(urls2, f)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    f.close()


if __name__ == '__main__':
    main()
