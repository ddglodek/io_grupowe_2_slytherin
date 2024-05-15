
# Testy

from main import wybierz_sowe_zwroc_koszt


assert(wybierz_sowe_zwroc_koszt(True, "lokalna", "list", "wyjec") == {'galeon': 0, 'sykl': 0, 'knut': 13})
print(wybierz_sowe_zwroc_koszt(True, "dalekobiezna", "list", None))
print(wybierz_sowe_zwroc_koszt(False, "krajowa", "paczka", None))
#testy dla przypadków niepoprawnych
print(wybierz_sowe_zwroc_koszt(True, "lokalna", "list", "")) # nieprawidłowy typ specjalnej przesyłki
print(wybierz_sowe_zwroc_koszt(True, "lokalna", "", "wyjec")) # nieprawidłowy typ przesyłki
print(wybierz_sowe_zwroc_koszt(True, "", "list", "wyjec")) # brak podanej odległości