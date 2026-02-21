class Bank:
    #Static / Class Members
    bname="Sbi"
    bloc="Hyd"
    bifsc=1122
    brating=4
    #Constructor to initialize object members
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
#Creating objects (3 Objects with 3 Object Members)
b1=Bank("Nitesh",123,2500)
b2=Bank("Avishek",124,2000)
b3=Bank("Raj",125,1500)

print(b1.name,b1.acc_no,b1.balance)
print(b2.name,b2.acc_no,b2.balance)
print(b3.name,b3.acc_no,b3.balance)