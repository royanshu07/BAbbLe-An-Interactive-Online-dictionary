from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def google(word):
    topic_search=word
    topic_search=topic_search.replace(' ','+')

    path=Service("D:\IT\BAbbLe-An-Interactive-Online-dictionary\chromedriver.exe")
    browser=webdriver.Chrome(service=path)
    for i in range(1):
        elements=browser.get("https://www.google.com/search?q="+topic_search+"&start"+str(i))

