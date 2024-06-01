import re
import sys
from termcolor import cprint 
from pyfiglet import figlet_format
from colorama import init
from itertools import cycle

def calculate_password_strength(password):
    length = len(password)

    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special_char = False

    for char in password:
        if char.islower():
            has_lowercase = True
        if char.isupper():
            has_uppercase = True
        if char.isdigit():
            has_digit = True
        if re.search(r'[!@#$%^&*(),.?":{}|<>] ', char):
            has_special_char = True

    complexity = 0

    if has_lowercase:
        complexity += 1
    if has_uppercase:
        complexity += 1
    if has_digit:
        complexity += 1
    if has_special_char:
        complexity += 1

    if length >= 8:
        complexity += 1
    if length >= 12:
        complexity += 1
    if length >= 16:
        complexity += 1

    if complexity < 3:
        return "Weak Password"
    elif complexity < 5:
        return "Medium Password"
    else:
        return "Strong Password"

def main():
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    cprint(figlet_format('PassComplex1.0'), 'red', 'on_black', attrs=['bold'])
    print("Welcome to PassComplex1.0 | Made by 6p@rtsXX | Prodigy CS-03")
    print("============================================================")
    print("Enter Password (or 'exit' to quit)\n")
    while True:
        password = input("==> ")
        if password.lower() == 'exit':
            break

        strength = calculate_password_strength(password)
        print(f"Strength: {strength}\n")

    print("Exiting the Password Strength Checker.")

if __name__ == "__main__":
    main()
