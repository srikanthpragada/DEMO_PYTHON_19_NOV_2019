class InvalidAmountError(Exception):
    def __init__(self, amount):
        self.message = f'Invalid transaction amount : {amount}'

    def __str__(self):
        return self.message


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
        if amount <= 0:
            raise InvalidAmountError(amount)

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


# print(Account.getminbal())  # call static method

a1 = Account(101, "Mr. Steve", 20000)  # Object
a2 = Account(102, "Mr. Larry")
try:
    a2.deposit(-10000)
    print(a2.availbal)  # Property
    a2.withdraw(300000)

    for ttype, tamt, bal in a2.transactions:
        print(ttype, tamt)
except Exception as ex:
    print(ex)
