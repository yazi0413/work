# -*- coding: utf-8 -*-

import urllib
import urllib2
import re

class spider:
    def __init__(self):
        self.siteURL='https://mm.taobao.com/json/request_top_list.htm'

    def getPage(self,pageIndex):
        url=self.siteURL+'?page='+str(pageIndex)
        print url
        request=urllib2.Request(url)
        response=urllib2.urlopen(request)
        return response.read().decode('gbk')
    def getContents(self,pageIndex):
        page=self.getPage(pageIndex)
        pattern=re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)"\
        .*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        items=re.findall(pattern,page)
        print items
        for item in items:
            print item[0]

spider=spider()
spider.getContents(1)
