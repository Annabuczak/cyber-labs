import random
import string

letters = "abcde"
numbers = "1,2,3,4,5,6,7,8,9,0"
symbols = "!@£$%^&*()_+-=<>?,./?;:"
print(random.choice(letters))
print(random.choice(numbers))
print(random.choice(symbols))

password = ""
for _ in range(12):
    password += random.choice(letters)
    password += random.choice(symbols)
    password += random.choice(numbers)

print(password)
print(password)
/Users/annabuczak/PycharmProjects/Cyber-labs

