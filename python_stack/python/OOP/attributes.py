class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

guido = User("Guido Van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

print(guido.name)
print(monty.name)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = 0

    def make_deposit(self, amount):
        self.account_balance += amount
