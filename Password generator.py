import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    letters = string.ascii_letters  # A-Z, a-z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # !@#$%^&*()_+ etc.

    characters = letters
    if use_digits:
        characters += digits
    if use_symbols:
        characters += symbols

    if not characters:
        return "No character types selected."

    # Ensure at least one of each selected type is included
    password = []
    if use_digits:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))
    password.append(random.choice(letters))

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    return ''.join(password)

def main():
    print("\n--- Password Generator ---")
    try:
        length = int(input("Enter password length (de
