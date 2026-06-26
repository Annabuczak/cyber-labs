correct_pin = "1234"
attempt_left = 3

while attempt_left > 0:
    user_pin = input("Please enter your PIN: ")

    if user_pin == correct_pin:
        print("Access granted.")
        break
    else:
        attempt_left -= 1
        print("Incorrect PIN.")

        if attempt_left == 0:
            print("Card is blocked. Contact provider")