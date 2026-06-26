

correct_pin = "1234"
attempt_left = 3
user_pin = input("Please enter your PIN: ")

correct_pin = "1234"
attempt_left = 3

user_pin = input("Please enter your PIN: ")

if user_pin == correct_pin:
    print("Access granted.")
else:
    print("Incorrect PIN.")

while attempt_left >0:
    user_pin = input("Please enter your PIN: ")
    if user_pin == correct_pin:
        print("Access granted.")
        break
    elif user_pin != correct_pin:
        print("Incorrect PIN.")
        attempt_left -= 1
        print("Card is blocked. Contact provider")
    else:
        break