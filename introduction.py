#coding=utf8
"""
# Author: quheng
# Created Time : Thu Oct 22 11:06:22 2015
"""
import urllib2
from bs4 import BeautifulSoup
import re
def get_html(url):
    flag = True
    while flag:
        try:
            page = urllib2.urlopen(url, timeout = 10)
            html = page.read()
            flag = False
        except Exception as e:
            print "try again"
            flag = True
    return html

def get_info(index):
    html = get_html(r'http://www.plantphoto.cn/sp/' + str(index))
    soup = BeautifulSoup(html)
    body = soup.body
    item =  body.select('#demodiv')[0]
    print str(html)
    result = str(item)
    res = re.compile("<div>(.*)</div>")
    return res.findall(result)

if __name__ == "__main__":
    f = open("res.txt","w")
    for i in xrange(1):
        print i
        #f.writelines(str(i))
        #f.writelines('\n')
        #f.writelines(get_info(i+48000))
        #f.writelines('\n')
        get_info(i+34518)

