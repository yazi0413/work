#-*- coding: utf-8 -*-
import urllib2
import json
from city_ import city

citycode=city.get('北京')
if citycode:
    url=('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
    content=urllib2.urlopen(url).read()
    #print content

data=json.loads(content)
result=data['weatherinfo']
str_temp=('%s\n%s~%s')%( result['weather'],result['temp1'],result['temp2'])
#print str_temp

url1='http://m.weather.com.cn/data5/city.xml'
content1=urllib2.urlopen(url1).read()
provinces=content1.split(',')

url='http://m.weather.com.cn/data3/city%s.xml'
for p in provinces:
    p_code=p.split('|')[0]
    url2=url%p_code
    content2=urllib2.urlopen(url2).read()
    #print content2
    cities=content2.split(',')
    print cities
