class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
        
    def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')
        
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')

owner=input()
balance=float(input())
z1=Account(owner, balance)
print(z1)
z1.owner
z1.balance
d=int(input())
z1.deposit(d)
w=int(input())
z1.withdraw(w)
l=int(input())
z1.withdraw(l)
