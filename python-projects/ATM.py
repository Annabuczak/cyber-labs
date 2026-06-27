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

class InvalidAmountError(Exception):
    pass

class InvalidAmountError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass


class CurrentAccount:
    def __init__(self, owner, balance,correct_pin):
        self.owner = owner
        self.balance = balance
        self.correct_pin = correct_pin

    def deposit(self,amount):

        self.balance += amount
        if amount <= 0:
            print("Incorrect amount.")
        else:
            print(f"Deposited £{amount} successfully!")
        return amount


    def withdraw(self,amount):
        if amount > 0:
            print("You don't have enough money!")
            raise InsufficientFundsError("Not enough funds.")

        else:
            self.balance -= amount
            print(f"Withdrew £{amount} successfully!")
            return amount

    def check_balance(self):
        if self.balance <= 0:
            print("Current balance!")
            return 0
        else:
           print(self.balance)

owner = "Louie"
start_balance = 0
account = CurrentAccount(owner, start_balance,correct_pin)


balance = account.check_balance()




while True:
    print("\n===== Bank of Anna =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    choice = input("Enter your choice: ")
    try:

        if choice == "1":
           amount = int(input("Enter amount to deposit: "))
           account.deposit(amount)
    except ValueError:
        print("Please enter numbers.")
        continue
    try:
        if choice == "2":
           amount = int(input("Enter amount to withdraw: "))
           account.withdraw(amount)
    except ValueError:
        print("Please enter numbers.")
        continue

    if choice == "3":
        account.check_balance()
    elif choice == "4":
        print("Thank you for using Bank of Anna. Goodbye")
    else:
        print("Goodbye.")
        break