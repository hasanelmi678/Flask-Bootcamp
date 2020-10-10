class BankAccount():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f'\nAccount Owner: {self.owner}\nBalance: ${self.balance}\n'
    
    def withdraw(self, amount):
        if amount > self.balance:
            print('\nNot enough money in your account.')
            print(f'Balance: ${self.balance}\n')
        else:
            self.balance -= amount
            print(f'\nWithdrew: ${amount}')
            print(f'Balance: ${self.balance}\n')
    
    def deposit(self, amount):
        self.balance += amount
        print(f'\nDeposited: ${amount}')
        print(f'Balance: ${self.balance}\n')


hasan = BankAccount('Hasan', 1000)
# print(hasan)
# print(hasan.owner)
# print(hasan.balance)

hasan.deposit(200)
print(hasan)

hasan.withdraw(800)
print(hasan)

hasan.withdraw(800)
print(hasan)