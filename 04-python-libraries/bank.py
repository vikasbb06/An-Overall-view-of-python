from account import Account
from database import Database


class Bank:
    def __init__(self):
        self.account = Database.load()

    def create_account(self):
        acc_no = input("Enter Account Number: ")
        if acc_no in self.account:
            print(f"Account Number {acc_no} already exists")
            return

        name = input("Enter Account holder Name: ")
        balance = float(input("Enter Initial Balance: "))
        account = Account(acc_no, name, balance)
        self.account[acc_no] = account
        Database.save(self.account)
        print(f"Account {acc_no} created successfully")

    def deposit(self):
        acc_no = input("Enter Account Number: ")
        if acc_no not in self.account:
            print("Account not found")
            return

        amount = float(input("Enter amount to deposit: "))
        self.account[acc_no].deposit(amount)
        Database.save(self.account)

    def withdraw(self):
        acc_no = input("Enter Account Number: ")
        if acc_no not in self.account:
            print("Account not found")
            return

        amount = float(input("Enter amount to withdraw: "))
        self.account[acc_no].withdraw(amount)
        Database.save(self.account)

    def check_balance(self):
        acc_no = input("Enter Account Number: ")
        if acc_no not in self.account:
            print("Account not found")
            return

        self.account[acc_no].check_balance()

    def display_account(self):
        acc_no = input("Enter Account Number: ")
        if acc_no not in self.account:
            print("Account not found")
            return

        self.account[acc_no].display()