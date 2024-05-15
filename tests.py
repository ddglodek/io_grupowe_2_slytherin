from main import *

dictionary = {
    "galeon": 14,
    "sykl": 9,
    "knut": 1
}

assert(waluta_dict_na_str(dictionary)== "14 galeonów 9 sykli 1 knut")

dictionary2 = {
    "sykl": 20,
    "knut": 400
}

assert(waluta_dict_na_str(dictionary2)== "20 sykli 400 knutów")

dictionary2 = {
    "galeon": 0,
    "sykl": 20,
    "knut": 400
}

assert(waluta_dict_na_str(dictionary2)== "20 sykli 400 knutów")

dictionary2 = {
    "galeon": 0,
    "sykl": 0,
    "knut": 0
}

assert(waluta_dict_na_str(dictionary2)== "Brak pieniędzy na koncie.")

dictionary = {
    "galeon": 1,
    "sykl": 3,
    "knut": 4
}

assert(waluta_dict_na_str(dictionary)== "1 galeon 3 sykle 4 knuty")


