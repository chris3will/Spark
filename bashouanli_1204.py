import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys
import random

#在12/5日由GYE指点,有的网站在一种条件下只对外发布有限篇内容，如本网站只最多显示500篇
pieces = 0  #下载的份数
pages = 0  #下载到了第几页

def dealevery():
    #对每一小页进行处理，即获取10份word
    add = 0
    x=random.randint(0,1)
    time.sleep(x)
    suba = driver.find_elements_by_css_selector(".generateWord.font-color")
    if (suba):
        for i in range(0,len(suba)-1):
            suba[i].click()
            add+=1
            #pieces += 1
            #print(pieces)
    else:
        print("该页无内容，终止行动!")
    return add

def tologin(a):
    #登陆函数
    account = "13036676783"
    password = "SCUZSL2018"
    a.find_element_by_id('mobile').send_keys(account)
    a.find_element_by_id('password').send_keys(password)
    btn = a.find_element_by_id('loginBtn')
    btn.click()



def dealwithmonth():
    pieces=0#下载数
    #2016年是闰年2-29
    monthday = {}
    monthday[1] = 31
    monthday[2]=28
    monthday[3] = 31
    monthday[5]=31
    monthday[7]=31
    monthday[8]=31
    monthday[10]=31
    monthday[12] = 31
    monthday[4] = 30
    monthday[6] = 30
    monthday[11] = 30
    monthday[9] = 30
    data0 = ""
    kk = 1  #月份
    while (kk <= 12 or int(data0.replace("-", "")) <= 20171231):
        print("这是",kk," 月")
        days = monthday[kk]
        fg=""
        if kk < 10:
            fg = "0{k}".format(k=kk)
        else:
            fg = "{k}".format(k=kk)
        data0 = "2017-{k}-01".format(k=fg)
        data1 = "2017-{k}-{a}".format(a=days,k=fg)
        #完成对每个月的初始化
        flag0,flag1=0,0
        #每个月默认的初始大循环
        flag0 = int(data0[-2]+data0[-1])#记录小循环的开始日期
        flag1 = int(data1[-2]+data1[-1])#记录小循环的终止日期
        js0="var begin=document.getElementById(\"judgementDateStart\").value=\"{begin1}\"".format(begin1=data0)
        js1="var end=document.getElementById(\"judgementDateEnd\").value=\"{end1}\"".format(end1=data1)
        driver.execute_script(js0)
        driver.execute_script(js1)
        time.sleep(1)

        btn=driver.find_element_by_id("advanceSearchBtn")
        btn.click()
        time.sleep(1.8)
        foundnum = driver.find_element_by_xpath("//span[contains(@id,'numFound')]").text

        tempmon = 0
        #print(flag1,flag0,monthday[kk])
        running = 1
        flap = 0
        foundnum = driver.find_element_by_xpath("//span[contains(@id,'numFound')]").text
        flap=int(foundnum)
        while (running):
            #确保完成每个月内的小循环
            print("当前正在处理第 ",kk," 月………………")
            
            
            print("当前flag如下: ",flag0,flag1)
            foundnum = driver.find_element_by_xpath("//span[contains(@id,'numFound')]").text
            print(foundnum)
            while (int(foundnum) > 500 and flag1>flag0):
                #只对同月操作,且只有当前查找数目大于500，能不一次性处理下才进行该循环得到可处理的数目
                flag1 -= 1
                data1 = data1[0:-2] + str(int(data1[-2] + data1[-1]) - 1)
                js1 = "var end=document.getElementById(\"judgementDateEnd\").value=\"{end1}\"".format(end1=data1)
                driver.execute_script(js1)
                btn=driver.find_element_by_id("advanceSearchBtn")
                btn.click()
                time.sleep(3)
                foundnum = driver.find_element_by_xpath("//span[contains(@id,'numFound')]").text
                print(foundnum)
        
            
            while (tempmon < int(foundnum)):
                time.sleep(1)
                a=dealevery()
                tempmon += a
                btn_next = driver.find_element_by_xpath("//a[contains(@rel,'next')]")
                btn_next.click()
                if (a == 0):
                    break
                print("本月已经下载 ",tempmon," 份.")
            
        
            if flap <= tempmon:
                running=0
            else:
                print("已到达本次搜索浏览上限，即50次.")
                time.sleep(1)
                data0 = "2017-{k}-{b}".format(k=fg,b=str(int(data1[-2] + data1[-1]) + 1))
                data1 = "2017-{k}-{a}".format(a=days, k=fg)
                flag0 = int(data0[-2]+data0[-1])#记录新小循环的开始日期
                flag1 = int(data1[-2] + data1[-1]) #记录新小循环的终止日期
            
                js0="var begin=document.getElementById(\"judgementDateStart\").value=\"{begin1}\"".format(begin1=data0)
                js1="var end=document.getElementById(\"judgementDateEnd\").value=\"{end1}\"".format(end1=data1)
                driver.execute_script(js0)
                driver.execute_script(js1)
                time.sleep(1)
            

        #准备看看是否进入下一个月
        pieces+=tempmon
        if flag1 == monthday[kk] :
            #这个月的内容已被处理完
            if kk == 12:
                print("结束")
            else:
                kk=kk+1
    #kk += 1  #对每一个月进行遍历，在每一次大循环下将案例遍历干净


os.makedirs('./bsword', exist_ok=True)
#初始化chrome插件,默认安装目录
#本来想在此处尝试能否在程序运行中修改默认下载地址，可以起到分类的作用，但好像不行
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": r"D:\code\tlpython\Spark\bsword",
    "download.prompt_for_download": False,
    "safebrowsing.enabled":True
})
global driver
driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver', chrome_options=chrome_options)
driver.get('http://www.lawsdata.com/?q=eyJtIjoiYWR2YW5jZSIsImEiOnsidGV4dHMiOlt7InR5cGUiOiJhbGwiLCJzdWJUeXBlIjoiIiwidmFsdWUiOiLmiJDpg73luILplKbmsZ/ljLrkurrmsJHms5XpmaIg57y65bitIn1dLCJjYXNlVHlwZSI6WyIyIl0sInByb2NlZHVyZUlkIjpbIjEiXSwiaW5zdHJ1bWVudFR5cGVJZCI6WyIxIl0sImp1ZGdlbWVudFllYXIiOiIyMDE3LTIwMTciLCJmdXp6eU1lYXN1cmUiOiIwIn0sInNtIjp7InRleHRTZWFyY2giOlsic2luZ2xlIl0sImxpdGlnYW50U2VhcmNoIjpbInBhcmFncmFwaCJdfX0=&s=')
#driver.get('http://www.lawsdata.com/?q=eyJtIjoiYWR2YW5jZSIsImEiOnsidGV4dHMiOlt7InR5cGUiOiJhbGwiLCJzdWJUeXBlIjoiIiwidmFsdWUiOiLmiJDpg73luILplKbmsZ/ljLrkurrmsJHms5XpmaIg57y65bitIn1dLCJjYXNlVHlwZSI6WyIyIl0sInByb2NlZHVyZUlkIjpbIjEiXSwiaW5zdHJ1bWVudFR5cGVJZCI6WyIxIl0sImp1ZGdlbWVudFllYXIiOiIyMDE0LTIwMTciLCJqdWRnZW1lbnREYXRlU3RhcnQiOiIyMDE3LTEyLTAxIiwianVkZ2VtZW50RGF0ZUVuZCI6IjIwMTctMTItMjAiLCJmdXp6eU1lYXN1cmUiOiIwIn0sInNtIjp7InRleHRTZWFyY2giOlsic2luZ2xlIl0sImxpdGlnYW50U2VhcmNoIjpbInBhcmFncmFwaCJdfX0=&s=')


time.sleep(3)
driver.maximize_window()
#发现登陆这个预先检索过的网址会自动弹出登陆窗口，于是不必模拟点击
#btn = driver.find_element_by_id('openLoginBtn')
#btn.click()

tologin(driver)
time.sleep(5)

#goal = int(input("你想下载多少份?"))

dealwithmonth()


#已经完成登陆，等待页面加载

'''
#下面为12/4的测试阶段
suba = driver.find_elements_by_css_selector(".generateWord.font-color")
if (suba):
    for i in range(0,len(suba)-1):
        suba[i].click()
'''



'''
while (pieces < goal):
    pieces += dealevery()
    print("已经下载 ",pieces," 份.")
    time.sleep(1)
    #if (pages - temp == 1):
    btn_next = driver.find_element_by_xpath("//a[contains(@rel,'next')]")
    if(btn_next):
        btn_next.click()
    else:
        print("已到达本次搜索浏览上限，即50次.")
    time.sleep(1)
'''

'''
#先输入想要查询的日期
if (driver):
    #这部分要试着实现自动控制
    data0 = (input("第一个地址: "))
    flag0=int(data0.replace("-",""))
    data1 = (input("第二个地址: "))
    flag1 = int(data1.replace("-", ""))
    print("尝试传值")


    js0="var begin=document.getElementById(\"judgementDateStart\").value=\"{begin1}\"".format(begin1=data0)
    js1="var end=document.getElementById(\"judgementDateEnd\").value=\"{end1}\"".format(end1=data1)
    driver.execute_script(js0)
    driver.execute_script(js1)
    
    btn=driver.find_element_by_id("advanceSearchBtn")
    btn.click()
    time.sleep(2)
    
    foundnum = driver.find_element_by_id("numFound").text
    print(foundnum)
    
    while (int(foundnum) > 500 and flag1>flag0):
        #只对同月操作
        flag1 -= 1
        data1 = data1[0:-2] + str(int(data1[-2] + data1[-1]) - 1)
        js1 = "var end=document.getElementById(\"judgementDateEnd\").value=\"{end1}\"".format(end1=data1)
        driver.execute_script(js1)
        btn=driver.find_element_by_id("advanceSearchBtn")
        btn.click()
        time.sleep(3)
        foundnum = driver.find_element_by_id("numFound").text
        print(foundnum)
        
    flag = {}
    flag[flag0]=flag1#把一组值记录下来
'''
