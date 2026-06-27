class Current_accout:
    def __init__(self,balance,deposit, withdraw,amount,owner):

        self.balance = balance
        self.deposit = deposit
        self.withdraw = withdraw
        self.amount = amount
        self.owner = owner
        self.balance = self.balance + self.deposit - self.withdraw
        print("Balance is: ", self.balance)

    def account_owner(self):
        print(
            f"Account holder {self.owner}, has {self.balance}, after paying in {self.deposit}, and taking out {self.withdraw}"
        )
        return self.balance + self.deposit - self.withdraw

    def withdraw_money(self):
       if amount.balance > amount.withdraw:
        print("You have enough money.")
       else:
        print("You do not have enough money.")


    def calculate_balance(self):
        return  self.balance + self.deposit - self.withdraw


    def amount(self,amount):
        if amount.amount(input) > amount.calculate_balance():
            print("You don't have enough money.")
        else:
            print("You have enough money.")



amount = Current_accout(balance=10000, deposit=1000, withdraw=10000,amount=100, owner="")
amount.account_owner()
amount.withdraw_money()
withdraw = amount.withdraw_money()