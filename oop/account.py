class Account:
    # class attribute or static variable
    minbal = 5000

    @staticmethod
    def getminbal():
        return Account.minbal

    # constructor
    def __init__(self, acno, ahname, balance=0):
        # object attributes
        self.acno = acno
        self.ahname = ahname
        self.balance = balance
        self.transactions = []

    # Methods
    def print(self):
        print("Acno        :", self.acno)
        print("Holder Name :", self.ahname)
        print("Balance     :", self.balance)

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(('d', amount, self.balance))

    def withdraw(self, amount):
        if self.balance - Account.minbal >= amount:
            self.balance -= amount
            self.transactions.append(('w', amount, self.balance))
        else:
            raise ValueError("Insufficient Balance!")

    # property
    @property
    def availbal(self):
        return self.balance - Account.minbal


print(Account.getminbal())  # call static method

a1 = Account(101, "Mr. Steve", 20000)  # Object
a2 = Account(102, "Mr. Larry")
a2.deposit(10000)
print(a2.availbal)   # Property

a2.withdraw(3000)

for ttype, tamt, bal in a2.transactions:
    print(ttype, tamt)
