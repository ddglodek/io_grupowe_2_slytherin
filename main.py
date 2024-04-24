import time
import random

def wyslij_sowe(adresat, tresc_listu):
    # adresat = input("Podaj adresata: ")
    # tresc_listu = input("Wpisz treść listu: ")
   
    powodzenie = random.choices([True, False], weights=[85, 15], k=1)[0]
    if powodzenie:
        time.sleep(1)  
        print(f"Wysyłam sowę do {adresat} z treścią: {tresc_listu}")
    return powodzenie
wyslij_sowe("Hagrid", "Wpadamy na herbate")

# i = 100
# while i > 0:
#     wyslij_sowe("Hagrid", "Wpadamy na herbate")
#     i -= 1