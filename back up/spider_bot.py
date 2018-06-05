# -*- coding: utf-8 -*-


##import urllib,urllib2
##
##url="https://api.douban.com/v2/movie/subject/1764798"
##response=urllib2.urlopen(url)
###print response.read()
##
##req=urllib.urlopen(url)
##info=req.info()
####print info
##charset=info.getparam('charset')
##content=req.read()
##print content.decode(charset,'ignore')

import urllib2
import urllib
import re

page=1
url='http://www.qiushibaike.com/hot/page/'+str(page)
user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent': user_agent}
try:
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    print response.read()
except urllib2.URLError, e:
    if hasattr(e,'code'):
        print e.code
    if hasattr(e,'reason'):
        print e.reason
        
content=response.read().decode('utf-8')
pattern= re.compile('h2>(.*?)</h2.*?content>(.*?)</.*?number>(.*?)</',re.S)
items=re.findall(pattern,content)
print items
for item in items:
    print item[0],item[1]
    

##' a test module '
##__author__='Chandler'
##
##import sys
##
##def test():
##    args=sys.argv
##    if len(args)==1:
##        print 'Hello world'
##    elif len(args)==2:
##        print 'Hello, %s' %args[1]
##    else:
##        print 'Too many arguments'
##
##if __name__=='__main__':
##    test()
##    
