class bank_account:
    all_accounts=[]
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        bank_account.all_accounts.append(self)
    @classmethod   
    def all_instances(cls):
        sum=0
        for account in cls.all_accounts:
            sum=account.balance
            print(f"Your Balance is ${sum}")
        return sum
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("insuficient funds: Charging a $5 fee")
            self.balance -= amount + 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance : ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance += (self.balance * self.int_rate)
        return self
    
class user:
    def __init__(self, name):
        self.name = name
        self.account = bank_account(int_rate=0.01, balance=0)
    def deposit(self, amount):
        self.account.deposit(amount)
        return self
    def withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    def display_account_info(self):
        self.account.display_account_info()
        return self

Checking=user("Alex")
Saving=user("Alex")

Checking.deposit(100).deposit(100).deposit(100).withdraw(350)
Saving.deposit(100).deposit(400).withdraw(50).withdraw(50).withdraw(50).withdraw(50)
bank_account.all_instances()
