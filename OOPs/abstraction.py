from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, customer_name, date_of_birth, balance):
        self.customer_name = customer_name
        self.date_of_birth = date_of_birth
        self.__balance = balance  

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass    

    def get_balance(self):
        print("Current Balance:", self.__balance)

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, dob, balance, minimum_balance):
        super().__init__(customer_name, dob, balance)
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self._BankAccount__balance += amount
        print("Amount Deposited")

    def withdraw(self, amount):
        if self._BankAccount__balance - amount >= self.minimum_balance:
            self._BankAccount__balance -= amount
            print("Amount Withdrawn")
        else:
            print("Minimum balance must be maintained")

class CurrentAccount(BankAccount):
    def __init__(self, customer_name, dob, balance, overdraft_limit):
        super().__init__(customer_name, dob, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        self._BankAccount__balance += amount
        print("Amount Deposited")

    def withdraw(self, amount):
        if self._BankAccount__balance - amount >= -self.overdraft_limit:
            self._BankAccount__balance -= amount
            print("Amount Withdrawn")
        else:
            print("Overdraft limit exceeded")

s1 = SavingsAccount("Rahul", "10-05-2000", 5000, 1000)
s1.deposit(1000)
s1.withdraw(4500)
s1.get_balance()

c1 = CurrentAccount("Amit", "15-08-1998", 3000, 2000)
c1.withdraw(4500)
c1.get_balance()