import random
import string
import time


def generate_random_code(length=24):
    """Generiert einen zufaelligen Promo-Code aus Buchstaben und Zahlen."""
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


def main():
    output_file = "Promo-Codes.txt"

    print("[+] Initializing generator...")

    try:
        num_codes = int(input("How many codes do you want to Generate? "))
        if num_codes <= 0:
            print("[!] Please enter a number greater than 0.")
            return
    except ValueError:
        print("[!] Invalid input. Please enter a whole number.")
        return

    print("[+] Generating Nitro Promo Codes...")
    print("[+] Status: UNCHECKED")

    start_time = time.time()

    with open(output_file, "w", encoding="utf-8") as file:
        for _ in range(num_codes):
            code = generate_random_code()
            link = f"https://discord.gift/{code}"
            print(f"[CODE] {link}")
            file.write(link + "\n")

    elapsed_time = time.time() - start_time
    speed = num_codes / elapsed_time if elapsed_time > 0 else num_codes

    print(f"[+] Speed: {speed:.0f} codes/sec")
    print(f"[+] Output saved to: {output_file}")


if __name__ == "__main__":
    main()
