def wyslij_sowe(adresat, tresc_listu):
   
    powodzenie = random.choices([True, False], weights=[85, 15], k=1)[0]
    if powodzenie:
        time.sleep(1)  
        print(f"Wysyłam sowę do {adresat} z treścią: {tresc_listu}")
    return powodzenie
wyslij_sowe("Hagrid", "Wpadamy na herbate")



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

print(licz_sume(fundusz))
import time
import random
