#coding=utf8
"""
# Author: quheng
# Created Time : Wed Oct 21 21:39:34 2015
"""

import urllib2
from bs4 import BeautifulSoup
import re

def get_html(url):
    flag = True
    while flag:
        try:
            page = urllib2.urlopen(url, timeout = 2)
            html = page.read()
            flag = False
        except:
            print "try again"
            flag = True
    return html

def get_name(index):
    html = get_html(r'http://www.plantphoto.cn/sp/' + str(index))
    soup = BeautifulSoup(html)
    body = soup.body
    item =  body.select('#demodiv > #result > .divpa2 > .fl')[0]
    result = str(item)
    res = re.compile("<div>(.*)</div>")
    return res.findall(result)

if __name__ == "__main__":
    f = open("res.txt","w")
    for i in xrange(1000):
        print i
        f.writelines(str(i))
        f.writelines(get_info(i+48000))
        f.writelines('\n')
