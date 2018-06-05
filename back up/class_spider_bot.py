# -*- coding: utf-8 -*-
import urllib
import urllib2
import re

#baidu 贴吧爬虫类
class BDTB:
    def __init__(self,baseUrl, seeLZ):
        self.baseURL=baseUrl
        self.seeLZ='?see_lz='+str(seeLZ)

    def getPage(self,pageNum):
        try:
            url=self.baseURL+self.seeLZ+'&pn='+str(pageNum)
            request=urllib2.Request(url)
            response=urllib2.urlopen(request)
##            print response.read()
            return response
        except urllib2.URLError,e:
            if hasattr(e,'reason'):
                print u"连接百度贴吧失败，错误原因",e.reason
                return None
    def getTitle(self):
        page=self.getPage(1)
       # <h1 class="core_title_txt  " title="纯原创我心中的NBA2014-2015赛季现役50大" style="width: 396px">纯原创我心中的NBA2014-2015赛季现役50大</h1>
        pattern=re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>',re.S)
        result=re.search(pattern,page)
        print result
        if result:
            print result.group(1)
            return result.group(1).strip()
        else:
            return None

baseURL='http://tieba.baidu.com/p/3138733512'
bdtb=BDTB(baseURL,1)
bdtb.getPage(1)
bdtb.getTitle
