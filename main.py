import random
import time
from typing import Dict, Any

def wyslij_sowe(adresat, tresc_listu):
   
    powodzenie = random.choices([True, False], weights=[85, 15], k=1)[0]
    if powodzenie:
        time.sleep(1)  
        print(f"Wysyłam sowę do {adresat} z treścią: {tresc_listu}")
    return powodzenie

def licz_sume(fund):
    galeon = fund.get("galeon", [0, 0, 0])
    sykl = fund.get("sykl", [0, 0, 0])
    knut = fund.get("knut", [0, 0, 0])

    sum_galeon = sum(galeon) * 17 * 21
    sum_sykl = sum(sykl) * 21
    sum_knut = sum(knut)

    suma = sum_galeon + sum_sykl + sum_knut

    # Przeliczanie na monety o największym nominale
    najwiekszy_nominal = suma // (17 * 21)
    suma %= (17 * 21)
    sredni_nominal = suma // 21
    suma %= 21

    return {
        "galeon": najwiekszy_nominal,
        "sykl": sredni_nominal,
        "knut": suma
    }

fundusz = {
    "galeon" : [1, 3, 5],
    "sykl" : [18, 20, 10],
    "knut" : [30, 40, 7]
}

def wybierz_sowe_zwroc_koszt(potwierdzenie_odbioru, odleglosc, typ, specjalna):
    koszt_gal = 0
    koszt_sykl = 0
    koszt_knut = 0

    if odleglosc == "lokalna":
        if typ == "list":
            koszt_knut += 2
        elif typ == "paczka":
            koszt_knut += 7
    elif odleglosc == "krajowa":
        if typ == "list":
            koszt_knut += 12
        elif typ == "paczka":
            koszt_knut += 2
            koszt_sykl += 1
    elif odleglosc == "dalekobiezna":
        if typ == "list":
            koszt_knut += 20
        elif typ == "paczka":
            koszt_knut += 1
            koszt_sykl += 2

    # Koszt potwierdzenia odbioru
    if potwierdzenie_odbioru:
        koszt_knut += 7

    # Koszty specjalne
    if specjalna == "wyjec":
        koszt_knut += 4
    elif specjalna == "list_gonczy":
        koszt_sykl += 1

    koszt_sykl += koszt_knut //  21
    koszt_knut = koszt_knut % 21

    koszt_gal += koszt_sykl // 17
    koszt_sykl = koszt_sykl % 17 

    koszt = {}

    koszt['galeon'] = koszt_gal
    koszt['sykl'] = koszt_sykl
    koszt['knut'] = koszt_knut


    return koszt

def waluta_dict_na_str(dictionary):
    
    sentence = ""
    
    tableKeys = list(dictionary.keys())
    
    tableVals = []
    for value in dictionary.values():
        tableVals.append(int(value))
        
    for index, key in enumerate(tableKeys):
        if "galeon" in key or "knut" in key:
            if tableVals[index] == 1:
                sentence += str(tableVals[index]) + " " + tableKeys[index] + " "
            elif tableVals[index] <= 0:
                sentence += ""
            elif 0 > tableVals[index] > 5:
                sentence += str(tableVals[index]) + " " + tableKeys[index] + "y "
            else:
                sentence += str(tableVals[index]) + " " + tableKeys[index] + "ów "
        if "sykl" in key:
            if tableVals[index] == 1:
                sentence += str(tableVals[index]) + " " + tableKeys[index] + " "
            elif tableVals[index] <= 0:
                sentence += ""
            elif 0 > tableVals[index] > 5:
                sentence += str(tableVals[index]) + " " + tableKeys[index] + "e "
            else:
                sentence += str(tableVals[index]) + " " + tableKeys[index] + "i "
                
    print(sentence)
    return sentence    
