import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
os.makedirs('./word',exist_ok=True)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": r"D:\code\tlpython\Spark\word",
    "download.prompt_for_download": False,
    "safebrowsing.enabled":True
})

with open('cookies.txt', 'r', encoding="utf-8") as f: 
    cookies_txt = f.read()
    #print(cookies_txt)
    saved_cookies = eval(cookies_txt)
    
driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver', chrome_options=chrome_options)

driver.get('https://www.itslaw.com/search?searchMode=judgements&sortType=1&conditions=searchWord%2B%E7%BC%BA%E5%B8%AD%2B1%2B%E7%BC%BA%E5%B8%AD&conditions=court%2B2542%2B1%2B%E6%88%90%E9%83%BD%E5%B8%82%E9%94%A6%E6%B1%9F%E5%8C%BA%E4%BA%BA%E6%B0%91%E6%B3%95%E9%99%A2&conditions=searchWord%2B%E4%B8%80%E5%AE%A1%2B1%2B%E4%B8%80%E5%AE%A1&conditions=searchWord%2B%E6%B0%91%E4%BA%8B%2B1%2B%E6%B0%91%E4%BA%8B')
for i in saved_cookies:
    driver.add_cookie(i)
time.sleep(15)

todown = driver.find_elements_by_css_selector(".fa.fa-download")
#print(todown)
for i in range(1, 30):
    todown[i].click()


