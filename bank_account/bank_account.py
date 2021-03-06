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
            print(f"Account Balance : ${sum}")
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
        
First_Account=bank_account()
Second_Account=bank_account()

First_Account.deposit(100).deposit(100).deposit(100).withdraw(350).yield_interest()
Second_Account.deposit(100).deposit(400).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest()
bank_account.all_instances()
