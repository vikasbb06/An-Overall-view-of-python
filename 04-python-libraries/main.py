from bank import Bank

bank = Bank()

while True:
    print("\n==================Welcome to Bank==================")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Display Account")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        bank.create_account()
    elif choice == "2":
        bank.deposit()
    elif choice == "3":
        bank.withdraw()
    elif choice == "4":
        bank.check_balance()
    elif choice == "5":
        bank.display_account()
    elif choice == "6":
        print("Thank you for using Bank")
        break
    else:
        print("Please enter a valid choice")