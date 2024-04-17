import time
import random

def wyslij_sowe():
    adresat = input("Podaj adresata: ")
    tresc_listu = input("Wpisz treść listu: ")
    print(f"Wysyłam sowę do {adresat} z treścią: {tresc_listu}")
    time.sleep(1)  
    powodzenie = random.choices([True, False], weights=[85, 15], k=1)[0]
    return powodzenie

wyslij_sowe()