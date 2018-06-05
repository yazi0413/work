#-*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import time

import sys
reload(sys)
sys.setdefaultencoding('utf-8') ##to avoid the confict between asscii and unicode



def findMaterial(Material_p,dict_material):
    temp=Material_p.find('li')
    while not temp==' ':
        temp1=temp.find('span')
        if not temp1.string==None:
            dict_material[temp1.previous_sibling.string]=temp1.string
            temp = temp.next_sibling
        if temp1.string==None:
            dict_material[temp1.previous_sibling.string] = 'null'
            temp = temp.next_sibling

##        material.append(temp1.previous_sibling.string)
##        value.append(temp1.string)






page=1
URL='http://www.meishij.net/chufang/diy/?&page='
url=[]
for page in range(1,10): ##collect the url
    response=urllib.urlopen(URL+str(page))
    time.sleep(5) # to avoid the website anti-robot forbidden
    soup=BeautifulSoup(response,'html.parser')
    ## add the program to find max page someday

    List=soup.find(class_='listtyle1')
    while not List==' ':
        url.append(List.find('a')['href'])
        List=List.next_sibling

for u in url:
    output = open('output_1_9_.txt', 'a')
    response=urllib.urlopen(u)
    soup=BeautifulSoup(response,'html.parser')

    if soup.find(id='tongji_title')==None: ## discard the null url
        output.close()
        continue
    CaiMing=soup.find(id='tongji_title').string
    GongYi=soup.find(id='tongji_gy').string
    NanDu=soup.find(id='tongji_nd').string
    RenShu=soup.find(id='tongji_rsh').string
    KouWei=soup.find(id='tongji_kw').string
    ZhunBeiTime=soup.find(id='tongji_zbsj').string
    PengRenTime=soup.find(id='tongji_prsj').string

    #作者的菜谱、关注、粉丝
    AuthorHot=soup.find(id='tongji_author').parent.next_sibling.next_sibling.string 
    #主料和辅料的父结点
    MainMaterial_p = soup.find(class_='yl zl clearfix')
    AssistMaterial_p=soup.find(class_='yl fuliao clearfix')

    MainMaterial={}
    AssistMaterial={}
    if not MainMaterial_p==None:
        findMaterial(MainMaterial_p,MainMaterial)
    if not AssistMaterial_p==None:
        findMaterial(AssistMaterial_p,AssistMaterial)

    ##Step
    Step_p=soup.find(class_='editnew edit')
    step=[]

    temp=Step_p.find(class_='content clearfix')
    while (not temp==' ') and (temp.name=='div'):
        temp_br=temp.find('p')
        if not temp_br.br==None: ## considering some node have <br/>
            step.append(temp_br.br.previous_sibling.string)

        step.append(temp_br.string)
        temp=temp.next_sibling.next_sibling

    # write into files
    output.write('菜名\t\t描述\t\t值\n')
    output.write(CaiMing+'\t工艺\t'+GongYi+'\n')
    output.write(CaiMing+'\t难度\t'+NanDu+'\n')
    output.write(CaiMing+'\t人数\t'+RenShu+'\n')
    output.write(CaiMing+'\t口味\t'+KouWei+'\n')
    output.write(CaiMing+'\t准备时间\t'+ZhunBeiTime+'\n')
    output.write(CaiMing+'\t烹饪时间\t'+PengRenTime+'\n')
    output.write(CaiMing+'\t活跃度\t'+AuthorHot+'\n')

    output.write(CaiMing+'\t主料：\n')
    for name in MainMaterial:
        output.write('\t\t\t\t'+name+': \t\t'+MainMaterial[name]+'\n')
    output.write(CaiMing+'\t辅料：\n')
    for name in AssistMaterial:
        output.write('\t\t\t\t'+name+': \t\t'+AssistMaterial[name]+'\n')

    output.write(CaiMing+'\t步骤：\n')
    i=1
    for st in step:
        if st==None: ## considering None has been appended into step list
            continue
        output.write('\t\t\t\t'+str(i)+st+'\n')
        i+=1

    output.write('\n\n\n')
    output.close()







