class User:
    def __init__(self):
        self.name = "Keith"
        self.account = 0
        self.account_balance =0

    def make_deposits(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self, amount):
        pass



elena = User()
elena.make_deposits(100)
elena.make_deposits(50)
elena.make_deposits(200)
elena.make_withdrawal(100)
print("Elena's balance is " + str(elena.account_balance))

bethany = User()
bethany.make_deposits(100)
bethany.make_deposits(100)
bethany.make_withdrawal(50)
bethany.make_withdrawal(50)
print("Bethany's balance is " + str(bethany.account_balance))


tito = User()
tito.make_deposits(100)
tito.make_withdrawal(20)
tito.make_withdrawal(20)
tito.make_withdrawal(20)
print("Tito's balance is " + str(tito.account_balance))