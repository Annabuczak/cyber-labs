import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

password = ""

for _ in range(12):
    password += random.choice(letters)
    password += random.choice(numbers)
    password += random.choice(symbols)

print("Generated Password:")
print(password)



import random

letters = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

length = int(input("Password length: "))

pool = letters

if input("Include uppercase letters? (y/n): ").lower() == "y":
    pool += uppercase

if input("Include numbers? (y/n): ").lower() == "y":
    pool += numbers

if input("Include symbols? (y/n): ").lower() == "y":
    pool += symbols

password = ""

for _ in range(length):
    password += random.choice(pool)

print("\nGenerated Password:")
print(password)