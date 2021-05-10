from requests import get
from bs4 import BeautifulSoup
import re


'https://www.morele.net/kategoria/karty-graficzne-12/,,,,,,,,0,,,,8143O1689340.974080/1/'

def morele():
    URL = 'https://www.morele.net/kategoria/karty-graficzne-12/,,,,,,,,0,,,,8143O1689348/1/'
    products = BeautifulSoup(get(URL).content, 'html.parser').find(class_ = 'cat-list-products').find_all('div', class_ = 'cat-product card')
    for product in products:
        
        price = product.find('div', class_ = 'price-new').text
        price = (re.sub('\D', '', price))
        name = product.find('a', class_ = 'productLink').get('title')
        link = product.find('a', class_ = 'productLink').get('href')
        link = f'https://www.morele.net{link}'
        
        print(price, name, link)
morele()