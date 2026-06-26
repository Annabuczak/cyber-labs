from typing import final

correct_pin = "1234"
attempt_left = 2

user_pin = input("Please enter your PIN: ")

if user_pin == correct_pin:
    print("Access granted.")
else:
    print("Incorrect PIN.")

while attempt_left >0:
    user_pin = input("Please enter your PIN: ")
    if user_pin == correct_pin:
        print("Access granted.")
    elif user_pin != correct_pin:
        print("Incorrect PIN.")
        attempt_left = 0
        print("Card is blocked. Contact provider")
    else:
        final()
