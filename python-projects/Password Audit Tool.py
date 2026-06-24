

password = input("Enter Password: ")
if len (password) >= 8:
     print("Password length passed")
else:
     print("Password is too short")



has_upper = False
for letter in password:
    if letter.isupper():
        has_upper = True
if has_upper:
    print("Password Has upper case letter")
else:
    print("Add an uppercase letter")

has_lower = False
for letter in password:
    if letter.islower():
        has_lower = True
if has_lower:
    print("Password Has lower case letter")
else:
    print("Add an lowercase letter")

has_numbers = False
for number in password:
    if number.isdigit():
        has_numbers = True
if has_numbers:
    print("Password has numbers")
else:
    print("Add an numbers")

has_symbols = False
for symbol in password:
    if symbol.isalpha():
        has_symbols = True
if has_symbols:
    print("Password has symbols")
else:
    print("Add an symbols")


password_strength = 0
if len(password) >= 8:
    password_strength += 1

if has_upper:
    password_strength += 1

if has_lower:
    password_strength += 1

if has_numbers:
    password_strength += 1

if has_symbols:
    password_strength += 1
print("Password Strength: " + str(password_strength))





