from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import random
import string
import urllib
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\Chromedriver\chromedriver.exe')

url = driver.get('https://www.instagram.com/ketikasharma/')

linkElem = driver.find_element_by_link_text('Load more')

type(linkElem)

linkElem.click()

htmlElem = driver.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)

soup = BeautifulSoup(urllib.op("https://www.instagram.com/ketikasharma/").read(), 'lxml')

div = soup.find('div', class_='_cmdpi')

for img in div.find_all('img'):
    print(img['src'])

    f = open(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(100))+'.jpg', 'wb')

    f.write(requests.get(img['src']).content)


f.close()

driver.quit()








