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
    def display(self):
        print(self.name, self.phone, self.balance)
    def withdraw(self, withdraw_bal):
        if self.balance>withdraw_bal:
            self.balance=self.balance-withdraw_bal
        else:
            print("Not enough balance")
    def deposit(self,deposit_bal):
        self.balance=self.balance+deposit_bal
b1=Bank("Nitesh",23,1987690808,"ABC",20000)
b2=Bank("Avishek",23,9999987654,"QAW",25000)
b3=Bank("Raj",23,1234565432,"WER",1500)

print(b1.name,b1.age,b1.phone,b1.pan,b1.balance)
print(b2.name,b2.age,b2.phone,b2.pan,b2.balance)
print(b3.name,b3.age,b3.phone,b3.pan,b3.balance)

b1.withdraw(5000)
b2.deposit(3000)
b3.withdraw(2000)

b1.display()
b2.display()
b3.display()