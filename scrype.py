from requests import get
from bs4 import BeautifulSoup
import re
from selenium import webdriver

GRAPRIC_CARDS = ('3060', '3070', '3080', '3090')

def morele():
    """Zwraca listę dostępnych kart do kupienia ze sklepu morele.pl"""

    URL = 'https://www.morele.net/kategoria/karty-graficzne-12/,,,,,,,,0,,,,8143O1689348.1689340.1689334.1728675.1760879/1/'
    products = BeautifulSoup(get(URL).content, 'html.parser').find(class_ = 'cat-list-products').find_all('div', class_ = 'cat-product card')
    final_list = []
    for product in products:
        price = product.find('div', class_ = 'price-new').text
        price = float((re.sub('\D', '', price)))
        name = product.find('a', class_ = 'productLink').get('title')
        link = product.find('a', class_ = 'productLink').get('href')
        link = f'https://www.morele.net{link}'
        card_model = 0
        for graphic_card in GRAPRIC_CARDS:
            if (graphic_card in name):
                card_model = graphic_card

        product_details = {
        'model' : card_model,
        'name': name,
        'price': price,
        'link': link,
        'sklep': 'morele'
        }

        final_list.append(product_details)
    return final_list

def xkom():
    """Zwraca listę dostępnych kart do kupienia ze sklepu xkom.pl"""

    LINK = 'https://www.x-kom.pl/g-5/c/346-karty-graficzne-nvidia.html?f%5B1702%5D%5B178114%5D=1&f%5B1702%5D%5B178141%5D=1'
    PATH = 'C:\Program Files (x86)\chromedriver.exe'  
    driver = webdriver.Chrome(PATH)
    driver.get(LINK)
    page = BeautifulSoup(driver.page_source, 'html.parser')
    final_list = []
    products = page.find_all(class_ = 'sc-162ysh3-1')
    for product in products:
        name = product.find('h3').get('title')
        link = product.find('a', class_ = 'sc-1h16fat-0').get('href')
        price = float(product.find(class_ = 'hNZEsQ').string.replace(' ','').replace('zł','').replace(',','.'))
        active = product.find(class_ = 'eNNpCW').get('disabled')

        if (active is None):
            card_model = 0
            for graphic_card in GRAPRIC_CARDS:
                if (graphic_card in name):
                    card_model = graphic_card

            product_details = {
            'model' : card_model,
            'name': name,
            'price': price,
            'link': link,
            'sklep': 'x-kom'
            }

            final_list.append(product_details)
    driver.close()
    return final_list

def media_expert():
    """Zwraca listę dostępnych kart do kupienia ze sklepu mediaexpert"""

    LINK = 'https://www.mediaexpert.pl/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/model_geforce-rtx-3060.geforce-rtx-3090.geforce-rtx-3080.geforce-rtx-3070.geforce-rtx-3060-ti'
    PATH = 'C:\Program Files (x86)\chromedriver.exe'
    final_list = []
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

        card_model = 'brak'
        for graphic_card in GRAPRIC_CARDS:
            if (graphic_card in name):
                card_model = graphic_card

        product_details = {
        'model' : card_model,
        'name': name,
        'price': price,
        'link': link,
        'sklep': 'media-expert'
        }

        final_list.append(product_details)
    driver.close()  
    return final_list

def sorting_list_model(data_list):
    """Sortuje listę według modelu karty graficznej"""

    sorted_dictionary = {
        '3060': [],
        '3070': [],
        '3080': [],
        '3090': [],
        'brak': []
    }

    for item in data_list:
        sorted_dictionary[item['model']].append(item)

    for model in sorted_dictionary:
        sorted_dictionary[model] = sorted(sorted_dictionary[model], key = lambda i: (i['price']))


    return sorted_dictionary