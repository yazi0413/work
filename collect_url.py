#-*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import time


URL='http://www.meishij.net/hongpei/?&page='

################################collect the url
url_f=open('url_hongpei.txt','w')

for page in range(1,57):
    response=urllib.urlopen(URL+str(page))
    time.sleep(5) # to avoid the website anti-robot forbidden
    soup=BeautifulSoup(response,'html.parser')
    ## add the program to find max page someday

    List=soup.find(class_='listtyle1')
    while not List==' ':
        url_f.write(List.find('a')['href']+'\n') ##write the link into text file
        print List.find('a')['href']
        List=List.next_sibling

url_f.close()
