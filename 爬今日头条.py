# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:01:28 2019
爬今日头条尝试
@author: Chris
"""
import requests
from bs4 import BeautifulSoup
import random
import time
from selenium import webdriver
import json
import re
import os
os.makedirs('G:/爬今日头条', exist_ok=True)

headers=[
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'},
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
    {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}
]
driver=webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe')

driver.get('https://www.toutiao.com')

time.sleep(1)

driver.maximize_window()
#print(driver.page_source)
rawlinks=driver.find_elements_by_xpath("//div[@class='title-box']/a")
links={}
def appendlist(dicc):
    for i in range(len(rawlinks)):
        tmp=rawlinks[i].get_attribute('href')
        print(tmp)
        #print(rawlinks[i].get_attribute('href'))#这个函数很关键
        tmp=tmp.replace('https://www.toutiao.com/group/','https://m.toutiao.com/i')
        tmp=tmp+"info/"
        if(tmp not in links):
            links[tmp]=1    
            #tmp=re.compile(pattern,tmp)
            #print(tmp)
            #http://m.toutiao.com/i6364969235889783298/info/
            
appendlist(links)
print(links)#得到了唯一的接口地址
mylink=[]
for i in links:
    mylink.append(i)
print(mylink)
ans_cmt_ipc_title=[]
with open("D:/爬今日头条/test.txt","w") as f:
    for i in mylink:
        req=requests.get(url=i,headers=random.choice(headers))#得到最原始的接口页面数据
        #print(req.encoding)
        #req.decode("unicode-escape")
        json_req=json.loads(req.text)
        print(type(req.text))
        comment_count=re.search(r'"comment_count":(.*?),',req.text)
        title=re.search(r'"title":"(.*?)",',req.text)
        title=title.group(1)
        impression_count=re.search(r'"impression_count":"(.*?)",',req.text)
        print(comment_count.group(1))
        tmp_cmt_ipc_title=[title,comment_count.group(1),impression_count.group(1)]#每个有三项元素
        #for k in json_req:
            #print(k,json_req[k],"\n*****")
            #print(type(json_req[k]),"thisistype")
            #print(type(k))
            #for j in k:
                #print(j)
            #if(k=='comment_count' or 'impression_count' or 'title'):
                #print(k,json_req[k])
                #tmp_cmt_ipc_title.append(json_req[k])
        ans_cmt_ipc_title.append(tmp_cmt_ipc_title)
        for i in tmp_cmt_ipc_title:
            #print(i)
            #print(type(i))
            f.write(i)
            f.write(",")
        
        f.write("\n")
        #print(json_req.get('comment_count'),json_req.get('impression_count'),json_req.get('title'))

print(ans_cmt_ipc_title)