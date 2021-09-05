from scrype import *
from prettytable import PrettyTable
import os

graphic_cards_list = sorting_list_model([*morele(), *media_expert()])

def your_choice():
    """Wybieranie zadania przez użytkownika"""

    global graphic_cards_list
    choice = input("""Co chcesz zrobić?
1 - Pokaż oferty dla wszystkich modeli (Max 3 sztuk)  3 - Pokaż najtańszą ofertę dla wybranego modelu
2 - Pokaż wszystkie oferty dla wybranego modelu       4 - Wczytaj dane ze stron
Wybór: """)
    if (choice == '1'):
        os.system('cls')
        create_table(graphic_cards_list)
        return

    elif (choice == '2' or choice == '3'):
        choice_model = input (""" 
Wybierz model: 
1 - RTX 3060   3 - RTX 3080
2 - RTX 3070   4 - RTX 3090
    """)
        if (choice_model == '1'):
            choice_model = '3060'
        elif (choice_model == '2'):
            choice_model = '3070'
        elif (choice_model == '3'):
            choice_model = '3080'
        elif (choice_model == '4'):
            choice_model = '3090'
        
        if(choice == '2'):
            choice = None

        create_table(graphic_cards_list, choice_model, choice)
        return
    
    elif(choice == '4'):
        graphic_cards_list = sorting_list_model([*morele(), *xkom(), *media_expert()])
        create_table(graphic_cards_list)
        return


def create_table(card_list, choice_model = None, choice = None):
    """Funkcja tworząca tabelę wyświetlającą oferty kart"""
    os.system('cls')
    cards_table = PrettyTable()

    #Wybrany model, wszystkie oferty (5 ofert)
    if (choice_model == None and choice == None):
        cards_table.field_names = ["Model", "Cena", "Nazwa", "Sklep"]
        for model in card_list:
            for card in card_list[model][0:3]:
                cards_table.add_row([card['model'], card['price'], card['name'].replace('Karta graficzna ', '')[0:20] + '..', card['sklep']])
    
    #Wybrany model, wszystkie oferty
    elif (choice_model != None and choice == None):
        cards_table.field_names = ["Model", "Cena", "Nazwa", "Sklep"]
        for card in card_list[choice_model]:
            cards_table.add_row([card['model'], card['price'], card['name'].replace('Karta graficzna ', '')[0:20] + '..', card['sklep']])

    #Wybrany model, pierwsza oferta
    elif (choice_model != None and choice == '3'):
        cards_table.field_names = ["Model", "Cena", "Nazwa", "Sklep"]
        for card in card_list[choice_model][0:1]:
            cards_table.add_row([card['model'], card['price'], card['name'].replace('Karta graficzna ', '')[0:20] + '..', card['sklep']])
    
    print(cards_table)
    your_choice()

create_table(graphic_cards_list)

