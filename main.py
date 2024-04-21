from typing import Dict, Any


def waluta_dict_na_str():
    
    dictionary: Dict[str, Any] = {"galeon": None, "sykl": None, "knut": None}
    
    galeony = input("Podaj ilosc galeonow: ")
    
    sykle = input("Podaj ilosc sykli: ")
    
    knuty = input("Podaj ilosc knutow: ")
    
    dictionary["galeon"] = galeony
    
    dictionary["sykl"] = sykle
    
    dictionary["knut"] = knuty
    
    print(dictionary)

waluta_dict_na_str()

