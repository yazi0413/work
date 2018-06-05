#-*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import time

import sys
reload(sys)
sys.setdefaultencoding('utf-8') ##to avoid the confict between asscii and unicode



def findMaterial(Material_p,dict_material):
    temp=Material_p.find('li')
    while (not temp==' ') and (not temp==None):
        temp1=temp.find('span')
        temp2=temp.find('h4').a
        if temp1.string==None:
            dict_material[temp1.previous_sibling.string] = 'null'
            temp = temp.next_sibling
        if not temp1.string==None:
            dict_material[temp2.string]=temp1.string
            if temp.next_sibling=='\n':
                temp=temp.next_sibling.next_sibling
                continue
            temp = temp.next_sibling

##        material.append(temp1.previous_sibling.string)
##        value.append(temp1.string)

url=[]
################# url has been collected into the 'url.txt'

################# now import the url

url_import=open('url_hongpei.txt','r') ###### !!!! check it now!!!
while True:
    line=url_import.readline()
    if line:
        url.append(line.strip())
    else:
        break
url_import.close()


start_p=open('start_position.txt','r+')
start=int(start_p.read())
start_p.seek(0)
error_flag=start
#################
for u in url[start:]:
    output = open('output_hongpei.txt', 'a') ###### !!!! check it now!!!
    response=urllib.urlopen(u)
    print 'getting '+u+'\n'
    time.sleep(10) # to avoid the website anti-robot forbidden
    soup=BeautifulSoup(response,'html.parser')

    ############### add error cases that need to change the start variant
    if not soup.find('div',class_='r_u_bot_main')==None:## if anti-hack works, record which url
        start_p.write(str(error_flag))
        output.close()
        break

    if soup.find(id='tongji_title')==None: ## discard the null url
        output.close()
        continue
    CaiMing=soup.find(id='tongji_title').string
    GongYi=soup.find(id='tongji_gy').string
    if soup.find(id='tongji_nd')==None:
        NanDu='unknown'
    if soup.find(id='tongji_nd')!=None:
        NanDu=soup.find(id='tongji_nd').string
    if soup.find(id='tongji_rsh') == None:
        RenShu = 'unknown'
    if soup.find(id='tongji_rsh') != None:
        RenShu=soup.find(id='tongji_rsh').string
    if soup.find(id='tongji_kw') == None:
        KouWei = 'unknown'
    if soup.find(id='tongji_kw') != None:
        KouWei=soup.find(id='tongji_kw').string
    if soup.find(id='tongji_zbsj') == None:
        ZhunBeiTime = 'unknown'
    if soup.find(id='tongji_zbsj') != None:
        ZhunBeiTime=soup.find(id='tongji_zbsj').string
    if soup.find(id='tongji_prsj') == None:
        PengRenTime = 'unknown'
    if soup.find(id='tongji_zbsj') != None:
        PengRenTime=soup.find(id='tongji_prsj').string

    #作者的菜谱、关注、粉丝
    if soup.find(id='tongji_author')==None:
        AuthorHot='Null'
    if soup.find(id='tongji_author')!=None:
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
    step = []
    Step_p=soup.find(class_='editnew edit')

    if not Step_p == None: ## new edit
        temp=Step_p.find(class_='content clearfix')
        while (not temp==' ') and (not temp==None) and (temp.name=='div'):
            temp_br=temp.find('p')
            if not temp_br.br==None: ## considering some node have <br/>
                if temp_br.br.previous_sibling==None:
                    step.append(temp_br.br.next_sibling.string)
                if temp_br.br.next_sibling==None:
                    step.append(temp_br.br.previous_sibling.string)

            step.append(temp_br.string)
            temp=temp.next_sibling.next_sibling

    if Step_p==None: ## old edit
        Step_p=soup.find(class_='edit')
        temp=Step_p.find('p')
        while(temp!='\n' and temp!=None):
            if(temp.em==None):
                if temp.next_sibling==None:
                    break
                temp=temp.next_sibling.next_sibling
                if temp=='\n':
                    break
            if(temp==None):
                break
            if(temp.em!=None):
                step.append(temp.em.next_sibling.string)
                temp=temp.next_sibling.next_sibling

        # while(not temp==None) and (temp!='\n'):
        #     if temp == ' ' or temp.next_sibling == None:
        #         break
        #     while (temp!=' ')and(temp.em==None) and temp.next_sibling!=None:
        #         temp=temp.next_sibling.next_sibling
        #
        #     step.append(temp.em.next_sibling.string)
        #     temp=temp.next_sibling.next_sibling



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
    print error_flag
    error_flag+=1

start_p.close()
