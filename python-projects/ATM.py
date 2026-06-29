import sys

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
            sys.exit()


class InvalidAmountError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass


class CurrentAccount:
    def __init__(self, owner, balance, correct_pin):
        self.owner = owner
        self.balance = balance
        self.correct_pin = correct_pin

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero.")
        self.balance += amount
        print(f"Deposited £{amount} successfully!")
        return amount

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero.")
        if amount > self.balance:
            raise InsufficientFundsError("Not enough funds.")

        self.balance -= amount
        print(f"Withdrew £{amount} successfully!")
        return amount

    def check_balance(self):
        print(f"Your current balance is: £{self.balance}")
        return self.balance


owner = "Louie"
start_balance = 0
account = CurrentAccount(owner, start_balance, correct_pin)

while True:
    print("\n===== Bank of Anna =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = int(input("Enter amount to deposit: "))
            account.deposit(amount)
        except ValueError:
            print("Please enter a valid number.")
        except InvalidAmountError as e:
            print(e)

    elif choice == "2":
        try:
            amount = int(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        except ValueError:
            print("Please enter a valid number.")
        except (InvalidAmountError, InsufficientFundsError) as e:
            print(e)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Thank you for using Bank of Anna. Goodbye.")
        break

    else:
        print("Invalid choice. Please try again.")