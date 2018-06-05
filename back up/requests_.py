import requests
import json

##r= requests.get('http://www.cuiqingcai.com')
##print type(r)
##print r.status_code
##print r.encoding
##print r.cookies
##
##payload={'key1':'value1','key2':'value2'}
##r=requests.get('http://httpbin.org/get',params=payload)
##print r.url

##r=requests.get('http://github.com/timeline.json',stream=True)
##print r.raw
##print r.raw.read(10)

##payload={'key1':'value1','key2':'value2','key3':'value3'}
##headers={'content-type':'application/json'}
##r=requests.get('http://httpbin.org/get',params=payload,headers=headers)
##print r.url
##
##r=requests.post('http://httpbin.org/post',data=payload)
##print r.text
##
##url='http://httpbin.org/post'
##files={'file':open('test.json','rb')}
##r=requests.post(url,files=files)
##print r.text

url='https://github.com'
r=requests.get(url,verify=True)
print r.text
