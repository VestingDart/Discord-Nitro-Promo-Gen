import random
import string


def generate_random_code(length=24):
    """Generiert einen zufaelligen Promo-Code aus Buchstaben und Zahlen."""
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


def main():
    output_file = "Promo-Codes.txt"

    try:
        num_codes = int(input("How many codes do you want to Generate? "))
        if num_codes <= 0:
            print("Pls enter a number.")
            return
    except ValueError:
        print("Ungueltige Eingabe. Bitte gib eine ganze Zahl ein.")
        return

    with open(output_file, "w", encoding="utf-8") as file:
        for _ in range(num_codes):
            code = generate_random_code()
            link = f"https://discord.gift/{code}"
            print(link)
            file.write(link + "\n")

    print(f"Codes wurden in '{output_file}' gespeichert.")


if __name__ == "__main__":
    main()
