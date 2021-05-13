from __future__ import print_function
from requests import get
from bs4 import BeautifulSoup
import re
from selenium import webdriver



def morele():
    URL = 'https://www.morele.net/kategoria/karty-graficzne-12/,,,,,,,,0,,,,8143O1689348/1/'
    products = BeautifulSoup(get(URL).content, 'html.parser').find(class_ = 'cat-list-products').find_all('div', class_ = 'cat-product card')
    for product in products:
        
        price = product.find('div', class_ = 'price-new').text
        price = (re.sub('\D', '', price))
        name = product.find('a', class_ = 'productLink').get('title')
        link = product.find('a', class_ = 'productLink').get('href')
        link = f'https://www.morele.net{link}'

        product_details = {
        'name': name,
        'price': price,
        'link': link
        }

        print(product_details)

def xkom():
    LINK = 'https://www.x-kom.pl/g-5/c/346-karty-graficzne-nvidia.html?f%5B1702%5D%5B178106%5D=1&f%5B1702%5D%5B178114%5D=1'
    PATH = 'C:\Program Files (x86)\chromedriver.exe'  
    driver = webdriver.Chrome(PATH)
    driver.get(LINK)
    page = BeautifulSoup(driver.page_source, 'html.parser')
    
    products = page.find_all(class_ = 'sc-162ysh3-1')
    for product in products:
        link = product.find('a', class_ = 'sc-1h16fat-0').get('href')
        price = product.find(class_ = 'hNZEsQ').string
        btn = product.find(class_ = 'eNNpCW').get('disabled')
        active_product = False
        if (btn == None):
            active_product = True
            print(price, link, active_product)
        elif(btn != None):
            active_product = False
        

        

def media_expert():
    
    LINK = 'https://www.mediaexpert.pl/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/model_geforce-rtx-3060.geforce-rtx-2080.geforce-rtx-2080-ti.geforce-rtx-2070.geforce-rtx-2060.geforce-rtx-3090.geforce-rtx-3080.geforce-rtx-3070.geforce-rtx-3060-ti'

    PATH = 'C:\Program Files (x86)\chromedriver.exe'
  
    
    driver = webdriver.Chrome(PATH)
    driver.get(LINK)
    page = BeautifulSoup(driver.page_source, 'html.parser')



    avilable_products = page.find_all(class_ = 'is-')
    avilavle_products2 = page.find_all(class_ = 'is-available')
    for product in avilavle_products2: 
        avilable_products.append(product)
    
    for product in avilable_products:
        name = product.find(class_ = 'is-col1').find(class_ = 'is-row2').find('a', class_ = 'a-typo is-secondary').string.strip()
        link = product.find(class_ = 'is-col1').find('a', class_ = 'a-typo is-secondary').get('href')
        price = int(product.find(class_ = 'a-price_new is-big').find(class_ = 'a-price_price').string.replace(' ',''))
        print(name, price, link)

     
morele()
xkom()
media_expert()


