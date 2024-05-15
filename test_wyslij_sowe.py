from main import wyslij_sowe

def test_wyslij_sowe_from_file():

      # type: ignore # Import the function from main.py
    
    sukcesy = 0
    total_attempts = 100
    
    while total_attempts > 0):
        if wyslij_sowe("Harry Potter", "Nie zapomnij o miotle!"):
            sukcesy += 1
        total_attempts -= 1
    print(f"Liczba udanych wysyłek: {sukcesy} z {total_attempts}")
    
    
test_wyslij_sowe_from_file()