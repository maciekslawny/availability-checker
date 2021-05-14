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


#graphic_cards_list = sorting_list_model([*morele(), *xkom(), *media_expert()])
#print(graphic_cards_list)

#print(sorting_list_model(graphic_cards_list))


# test_list = [{'model': '3070', 'name': 'Karta graficzna MSI GeForce RTX 3070 Gaming X Trio 8GB GDDR6 (RTX 3070 GAMING X TRIO)', 'price': 8999, 'link': 'https://www.morele.net/karta-graficzna-msi-geforce-rtx-3070-gaming-x-trio-8gb-gddr6-rtx-3070-gaming-x-trio-7244535/'}, {'model': '3070', 'name': 'Karta graficzna Gigabyte GeForce RTX 3070 Gaming OC 8GB GDDR6 (GV-N3070GAMING OC-8GD)', 'price': 8489, 'link': 'https://www.morele.net/karta-graficzna-gigabyte-geforce-rtx-3070-gaming-oc-8gb-gddr6-gv-n3070gaming-oc-8gd-5944660/'}, {'model': '3070', 'name': 'Karta graficzna MSI GeForce RTX 3070 Ventus 3X OC 8GB GDDR6 (RTX 3070 VENTUS 3X OC)', 'price': 7999, 'link': 'https://www.morele.net/karta-graficzna-msi-geforce-rtx-3070-ventus-3x-oc-8gb-gddr6-rtx-3070-ventus-3x-oc-7244536/'}, {'model': '3070', 'name': 'Karta graficzna Gigabyte Aorus GeForce RTX 3070 Master 8GB GDDR6 (GV-N3070AORUS M-8GD)', 'price': 8489, 'link': 'https://www.morele.net/karta-graficzna-gigabyte-aorus-geforce-rtx-3070-master-8gb-gddr6-gv-n3070aorus-m-8gd-7244534/'}, {'model': '3070', 'name': 'Karta graficzna Gigabyte GeForce RTX 3070 Vision OC 8GB GDDR6 (GV-N3070VISION OC-8GD)', 'price': 8389, 'link': 'https://www.morele.net/karta-graficzna-gigabyte-geforce-rtx-3070-vision-oc-8gb-gddr6-gv-n3070vision-oc-8gd-7244533/'}, {'model': '3070', 'name': 'Karta graficzna Asus TUF GeForce RTX 3070 Gaming OC 8GB GDDR6 (TUF-RTX3070-O8G-GAMING)', 'price': 8689, 'link': 'https://www.morele.net/karta-graficzna-asus-tuf-geforce-rtx-3070-gaming-oc-8gb-gddr6-tuf-rtx3070-o8g-gaming-7244531/'}, {'model': '3070', 'name': 'Karta graficzna Palit GeForce RTX 3070 JetStream 8GB GDDR6 (NE63070019P2-1040J)', 'price': 8389, 'link': 'https://www.morele.net/karta-graficzna-palit-geforce-rtx-3070-jetstream-8gb-gddr6-ne63070019p2-1040j-5945386/'}, {'model': '3070', 'name': 'Karta graficzna Zotac GeForce RTX 3070 Twin Edge OC White Edition 8GB GDDR6 (ZT-A30700J-10P)', 'price': 7989, 'link': 'https://www.morele.net/karta-graficzna-zotac-geforce-rtx-3070-twin-edge-oc-white-edition-8gb-gddr6-zt-a30700j-10p-7698851/'}, {'model': '3070', 'name': 'Karta graficzna Gainward GeForce RTX 3070 Phantom 8GB GDDR6 (471056224-2171)', 'price': 8369, 'link': 'https://www.morele.net/karta-graficzna-gainward-geforce-rtx-3070-phantom-8gb-gddr6-471056224-2171-7698846/'}, {'model': '3070', 'name': 'Karta graficzna Zotac GeForce RTX 3070 Twin Edge OC 8GB GDDR6 (ZT-A30700H-10P)', 'price': 7999, 'link': 'https://www.morele.net/karta-graficzna-zotac-geforce-rtx-3070-twin-edge-oc-8gb-gddr6-zt-a30700h-10p-7463163/'}, {'model': '3070', 'name': 'Karta graficzna Inno3D GeForce RTX 3070 Twin X2 OC 8GB GDDR6 (RTX 3070 TWIN X2 OC)', 'price': 8499, 'link': 'https://www.morele.net/karta-graficzna-inno3d-geforce-rtx-3070-twin-x2-oc-8gb-gddr6-rtx-3070-twin-x2-oc-7698848/'}, {'model': '3070', 'name': 'Karta graficzna MSI GeForce RTX 3070 Suprim X 8GB GDDR6 (RTX 3070 SUPRIM X 8G)', 'price': 8299, 'link': 'https://www.morele.net/karta-graficzna-msi-geforce-rtx-3070-suprim-x-8gb-gddr6-rtx-3070-suprim-x-8g-5945714/'}, {'model': '3070', 'name': 'Karta graficzna Zotac GeForce RTX 3070 AMP Holo 8GB GDDR6 (ZT-A30700F-10P)', 'price': 8189, 'link': 'https://www.morele.net/karta-graficzna-zotac-geforce-rtx-3070-amp-holo-8gb-gddr6-zt-a30700f-10p-7698850/'}, {'model': '3090', 'name': 'Karta graficzna NVIDIA KFA2 GeForce RTX 3090 HOF 24GB GDDR6X', 'price': 14999.0, 'link': '/p/647316-karta-graficzna-nvidia-kfa2-geforce-rtx-3090-hof-24gb-gddr6x.html'}, {'model': '3060', 'name': 'Karta graficzna MSI GeForce RTX 3060 Gaming X Trio 12GB', 'price': 4799, 'link': '/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/karta-graficzna-msi-geforce-rtx-3060-gaming-x-trio-12gb'}, {'model': '3070', 'name': 'Karta graficzna MSI GeForce RTX 3070 Gaming X Trio 8GB GDDR6', 'price': 7499, 'link': '/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/karta-graficzna-msi-geforce-rtx-3070-gaming-x-trio'}, {'model': '3090', 'name': 'Karta graficzna MSI GeForce RTX 3090 Suprim X 24GB', 'price': 15999, 'link': '/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/karta-graficzna-msi-geforce-rtx-3090-suprim-x-24g'}, {'model': '3060', 'name': 'Karta graficzna MSI GeForce RTX 3060 Gaming X 12GB', 'price': 4699, 'link': '/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/karta-graficzna-msi-geforce-rtx-3060-gaming-x-12gb'}]


#sorting_list_model(test_list)



