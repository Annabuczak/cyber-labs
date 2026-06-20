import random

random_letters = "abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
random_numbers = "1234567890"
random_symbols = "!@£$%^&*()_+-=<>?,./?;:"


password_length = int(input("How long do you want your password to be? "))

letters_choice = input("Do you want to use random letters y/n? ").lower()
if letters_choice == "y":
    letters = random_letters
else:
    letters = input("Enter the letters you want to use: ")

numbers_choice = input("Do you want to use random numbers y/n? ").lower()
if numbers_choice == "y":
    numbers = random_numbers
else:
    numbers = input("Enter the numbers you want to use: ")

symbols_choice = input("Do you want to use random symbols y/n? ").lower()
if symbols_choice == "y":
    symbols = random_symbols
else:
    symbols = input("Enter the symbols you want to use: ")

characters = letters + numbers + symbols

password = ""
for _ in range(password_length):
    password += random.choice(characters)

print(password)
