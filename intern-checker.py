#!/usr/bin/env python3

from selenium import webdriver
import bs4
# import pickle
from time import sleep
# import pdb

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('user-data-dir=/home/g/temp/intern/Default')
chrome_options.add_argument('class=selenium-chrome')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('http://www.internshala.com')

sleep(2)
html = driver.page_source
driver.close()
soup = bs4.BeautifulSoup(html, 'lxml')

for tag in soup.find_all('div'):
    try:
        tagClass = tag['class'][0]
    except:
        continue
    if tagClass == 'tooltiptextcontainer':
        print(tag.contents[0], end=' ')
print()
