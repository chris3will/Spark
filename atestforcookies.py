from selenium import webdriver
import requests
import time


headers={"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
manual_cookies={}
driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver')
driver.maximize_window()
with open('cookies.txt', 'r', encoding="utf-8") as f: 
    cookies_txt = f.read()
    print(cookies_txt)
    saved_cookies=eval(cookies_txt)
    
''' 
    for i in saved_cookies:
        for k in ('name', 'value', 'domain', 'path', 'expiry'):
            if k not in list(i.keys()):
                if k == 'expiry' and i[k] == '1540948771':
                    i[k]=int(i[k])
'''               
       

    


driver.get('https://www.itslaw.com/search?searchMode=judgements&sortType=1&conditions=searchWord%2B%E7%BC%BA%E5%B8%AD%2B1%2B%E7%BC%BA%E5%B8%AD&conditions=court%2B2542%2B1%2B%E6%88%90%E9%83%BD%E5%B8%82%E9%94%A6%E6%B1%9F%E5%8C%BA%E4%BA%BA%E6%B0%91%E6%B3%95%E9%99%A2&conditions=searchWord%2B%E4%B8%80%E5%AE%A1%2B1%2B%E4%B8%80%E5%AE%A1&conditions=searchWord%2B%E6%B0%91%E4%BA%8B%2B1%2B%E6%B0%91%E4%BA%8B')
for i in saved_cookies:
    driver.add_cookie(i)
time.sleep(10)
#btn_first = driver.find_element_by_css_selector("img[class='hide-tip']")
#btn_first.click()
time.sleep(10)
#conten = driver.find_element_by_class_name('tagit-new')
string = input("请输入你想查询的内容\n")
conten.send_keys(string)
sousuo = driver.find_element_by_class_name("search-button")
sousuo.click()

#driver.refresh()        '''