class User:
    
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        
Alex = User("Alex")
Bianca = User("Bianca")
Daniel = User("Daniel")

Alex.make_deposit(100)
Alex.make_deposit(200)
Alex.make_deposit(50)
Alex.make_withdrawl(45)
Alex.display_user_balance()

Bianca.make_deposit(1000)
Bianca.make_deposit(1000)
Bianca.make_withdrawl(500)
Bianca.make_withdrawl(300)
Bianca.display_user_balance()

Daniel.make_deposit(1500)
Daniel.make_withdrawl(1000)
Daniel.make_withdrawl(5000)
Daniel.make_withdrawl(3000)
Daniel.display_user_balance()


Alex.transfer_money(400, Daniel)
