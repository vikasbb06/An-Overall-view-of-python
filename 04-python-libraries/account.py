class Account:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited Successfully")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Amount Withdraw Successfully")

    def check_balance(self):
        print(f"Current balance :{self.balance}")

    def display(self):
        print(f"Account Name :{self.name}")
        print(f"Account Balance :{self.balance}")
        print(f"Account No. :{self.acc_no}")