import random
import string

def generate_random_code(length=24):
    """Generiert einen zufälligen Promo-Code aus Buchstaben und Zahlen."""
    characters = string.ascii_letters + string.digits  # Klein- und Großbuchstaben sowie Ziffern
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    # Frage den Benutzer, wie viele Codes generiert werden sollen
    try:
        num_codes = int(input("How many codes do you want to Generate? "))
        if num_codes <= 0:
            print("Pls enter a number.")
            return
    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine ganze Zahl ein.")
        return

    # Generiere die angegebene Anzahl von Codes
    for _ in range(num_codes):
        code = generate_random_code()  # Generiere einen zufälligen Code
        link = f"https://discord.gift/{code}"  # Erstelle den Link
        print(link)  # Gib den Link aus

if __name__ == "__main__":
    main()