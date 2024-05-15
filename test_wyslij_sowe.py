from main import wyslij_sowe

def test_wyslij_sowe_from_file():

      # type: ignore # Import the function from main.py
    
    sukcesy = 0
    total_attempts = 10
    
    for _ in range(total_attempts):
        if wyslij_sowe("Harry Potter", "Nie zapomnij o miotle!"):
            sukcesy += 1

    print(f"Liczba udanych wysyłek: {sukcesy} z {total_attempts}")
    return sukcesy/total_attempts 
    
    
assert(0.8 <= test_wyslij_sowe_from_file() <= 0.9)