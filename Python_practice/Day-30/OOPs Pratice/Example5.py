"""Question 5: Private Attributes

Question: Define a class Account with a private attribute balance. Provide methods to deposit and withdraw money and display the balance.
"""

class Account:
    def __init__(self,bal):
        self.__bal=bal

    def deposit(self, amount):
        self.__bal += amount

    def withdraw(self, amount):
        if amount <= self.__bal:
            self.__bal -= amount
        else:
            print("Insufficient balance")


    def display_balance(self):
        print(f"Balance:{self.__bal}")

initial_balance = float(input("Enter initial balance: "))
account = Account(initial_balance)

deposit_amount = float(input("Enter amount to deposit: "))
account.deposit(deposit_amount)
account.display_balance()

withdraw_amount = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount)
account.display_balance()
