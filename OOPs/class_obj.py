class Bank:
    bname="Sbi"
    bloc="Hyd"
    bifsc=1122
    brating=4
    def account(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
b1=Bank()
b2=Bank()
b3=Bank()

b1.account("Nitesh",123,2500)
b2.account("Avishek",124,2000)
b3.account("Raj",125,1500)

print(Bank.bname,Bank.bloc,Bank.bifsc,Bank.brating,b1.name,b1.acc_no,b1.balance)
print(Bank.bname,Bank.bloc,Bank.bifsc,Bank.brating,b2.name,b2.acc_no,b2.balance)
print(Bank.bname,Bank.bloc,Bank.bifsc,Bank.brating,b3.name,b3.acc_no,b3.balance)