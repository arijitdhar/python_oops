__author__ = '220152'

class Account():

    def __init__(self, filepath):
        self.filepath=filepath
        self.name = ">>Account"
        with open(filepath, 'r') as file:
            # balance is an instance variable, which is specific to an instance of the class
            self.balance = int(file.read())

    def withdraw(self, amount):
        print("Inside parent withdraw amount")
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    """
    Checking subclass extending Account base class
    """

    # This is class variable which would be used across all instances of the class, kind of static
    type="checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee
        # Overriding instance variable
        self.name = ">>Checking"

    def withdraw(self, amount):
        print("Inside overriden withdraw method")
        Account.withdraw(self, amount)

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


jacks_checking = Checking("jack.txt", 1)
jacks_checking.withdraw(100)
jacks_checking.commit()
print(jacks_checking.balance)
print(jacks_checking.type)
print(jacks_checking.name)


johns_checking = Checking("john.txt", 1)
johns_checking.transfer(100)
johns_checking.commit()
print(johns_checking.balance)
print(johns_checking.type)
print(johns_checking.name)



# __doc__ generates docstring for a class
print(jacks_checking.__doc__)




