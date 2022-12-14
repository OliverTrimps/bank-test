class Account:
    def __init__(self):
        self.account = []
        self.user_name = ""
        self.balance = 0
        self.available_balance = 0
        self.account_number = ""
        self.receiver = []

    def show_menu(self, acc_name, user):
        for name in acc_name:
            if name["name"] == user:
                self.account.append(name)
                self.user_name = name['name']
                self.available_balance = name['available balance']
                self.balance = name['balance']
                self.account_number = name['account number']
                return f"Welcome!\nš¤: {name ['name']}\nā°: {name['date']}\nš°: {name['balance']}"

    def get_balance(self):
        return f"Available Balance š°: {self.available_balance}"

    def deposit(self, amount):
        self.balance += amount
        self.available_balance += amount
        return f"Your deposit of {amount} is successful! š"

    def withdraw(self, amount):
        if amount > self.available_balance:
            return "Insufficient Funds! ā"
        else:
            self.balance -= amount
            self.available_balance -= amount
            return "Successful! š"

    def transfer(self, send, receiver, users):
        if send > self.available_balance:
            return "Your account balance is not sufficient to make this transfer! ā"
        for account in users:
            if account['account number'] == receiver:
                self.receiver.append(account)
                self.available_balance -= send
                self.balance -= send

                account['balance'] += send
                account['available balance'] += send
                return f"Your Transfer to {account['name']} is Successful! š"
        if self.receiver[0]['account number'] != receiver:
            return f"The account number {receiver} is invalid! ā"
