from datetime import datetime
from account import Account

date = datetime.now()
date_now = date.strftime("%d/%m/%Y")
# print(date_now)
users = [
    {
        "name": "Tom Holland",
        "account number": "1234567890",
        "balance": 7000,
        "available balance": 6950,
        "date": date_now,
    },
    {
        "name": "James Philip",
        "account number": "1244567890",
        "balance": 300,
        "available balance": 250,
        "date": date_now,
    },
    {
        "name": "Lone Wolf",
        "account number": "1233567890",
        "balance": 300000,
        "available balance": 299950,
        "date": date_now,
    },
]

user_name = input("Enter your account name: ").title()
account = Account()

print(account.show_menu(users, user_name))
# print(account.account)
running = True
while running:

    option = input("A(Available Balance 💰), D(Deposit 💵), W(Withdraw 💳), T(Transfer 💵) END(Logout 🔚): ").upper()
    if option == "A":
        print(account.get_balance())
    elif option == "D":
        amount = int(input("Enter your deposit amount 💵: "))
        print(account.deposit(amount))
    elif option == "W":
        amount = int(input("How much would you like to withdraw? 💳: "))
        print(account.withdraw(amount))
    elif option == "T":
        amount = int(input("Enter amount 💵: "))
        receiver = input("Enter receiver's account number 👤: ")
        print(account.transfer(amount, receiver, users))
    elif option == "END":
        print("Logout Successful! 👍")
        running = False
