
# Testy

from main import wybierz_sowe_zwroc_koszt


assert(wybierz_sowe_zwroc_koszt(True, "lokalna", "list", "wyjec") == {'galeon': 0, 'sykl': 0, 'knut': 13})
assert(wybierz_sowe_zwroc_koszt(True, "dalekobiezna", "list", None) == {'galeon': 0, 'sykl': 1, 'knut': 6})
assert(wybierz_sowe_zwroc_koszt(False, "krajowa", "paczka", None) == {'galeon': 0, 'sykl': 1, 'knut': 2})
#testy dla przypadków niepoprawnych
assert(wybierz_sowe_zwroc_koszt(True, "lokalna", "list", "") == {'galeon': 0, 'sykl': 0, 'knut': 9})# nieprawidłowy typ specjalnej przesyłki
assert(wybierz_sowe_zwroc_koszt(True, "lokalna", "", "wyjec") == {'galeon': 0, 'sykl': 0, 'knut': 11})# nieprawidłowy typ przesyłki
assert(wybierz_sowe_zwroc_koszt(True, "", "list", "wyjec") == {'galeon': 0, 'sykl': 0, 'knut': 11})# brak podanej odległości