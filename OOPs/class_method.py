class Bank:
    bname="Sbi"
    branch="Hyd"
    ifsc="SBIN00123"
    helpline="1800-11-2211"
    def __init__(self, name, age, phone, pan, balance):
        self.name=name
        self.age=age
        self.phone=phone
        self.pan=pan
        self.balance=balance

    def withdraw(self, withdraw_bal):
        if self.balance>withdraw_bal:
            self.balance=self.balance-withdraw_bal
        else:
            print("Not enough balance")
    def deposit(self,deposit_bal):
        self.balance=self.balance+deposit_bal
    @classmethod
    def change_age(cls, self, new_age):
        self.age = new_age
        print("Age updated successfully")

b1 = Bank("Nitesh", 23, 1987690808, "ABC", 20000)
b2 = Bank("Avishek", 23, 9999987654, "QAW", 25000)
b3 = Bank("Raj", 23, 1234565432, "WER", 1500)

Bank.change_age(b1, 30)
print(b1.name, b1.age)