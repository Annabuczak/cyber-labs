print("Welcome to Bank of Anna.")
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


class CurrentAccount:
    def __init__(self, owner, balance,correct_pin):
        self.owner = owner
        self.balance = balance
        self.correct_pin = correct_pin

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.balance += amount
        if amount <= 0:
            print("Incorrect amount.")
        else:
            print(f"Deposited £{amount} successfully!")
        return amount


    def withdraw(self):
        amount = int(input("How much would you like to withdraw? "))
        if amount > self.balance:
            print("You don't have enough money!")
            return 0
        else:
            self.balance -= amount
            print(f"Withdrew £{amount} successfully!")
            return amount

    def check_balance(self):
        return self.balance


owner = "Louie"
start_balance = 0
account = CurrentAccount(owner, start_balance,correct_pin)

deposited_amount = account.deposit()
withdrawn_amount = account.withdraw()
balance = account.check_balance()

print(
    f"{owner}'s balance is £{balance}. "
    f"{owner} has deposited £{deposited_amount}. "
    f"{owner} has withdrawn £{withdrawn_amount}."
)


