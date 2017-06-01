#coding:utf-8
'''采集京东商场手机价格（2500-2999）'''
import urllib2
import cookielib
import re

def chou_url(hosturl,headers,number,posturll,posturl2,restr):
    #hosturl = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exprice_M2500L2999&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main'
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    h = urllib2.Request(hosturl)

    url_list = []
    for i in xrange(1, number):
        # posturl = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exprice_M2500L2999&page=' + str(i) + ''
        posturl = posturll + str(i) + posturl2
        req = urllib2.Request(posturl)
        for key in headers:
            req.add_header(key, headers[key])
        html = urllib2.urlopen(req).read()
        # print html

        find_url = re.findall(restr, html)
        for item in find_url:
            x = item.find('"')
            if x > 0:
                out = item[:x]
            else:
                out = item
            url_list.append('https://item.jd.com'+out)
    return url_list

if __name__ == '__main__':
    hosturl = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exprice_M2500L2999&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main'
    headers =   {
                'Host':'list.jd.com',
                'Referer':'https://list.jd.com/list.html?cat=9987,653,655&ev=exprice%5FM2500L2999&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0',
                'Upgrade-Insecure-Requests':1,
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
                }
    number = 9
    posturl1 = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exprice_M2500L2999&page='
    posturl2 = ''
    restr = r'href="//item.jd.com(.*?)">'

    shouji_url = chou_url(hosturl,headers,number,posturl1,posturl2,restr)
    for item in shouji_url:
        print item
