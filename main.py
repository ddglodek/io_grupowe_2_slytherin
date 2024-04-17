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

# Przykładowe użycie funkcji
print(wybierz_sowe_zwroc_koszt(True, "lokalna", "list", "wyjec"))