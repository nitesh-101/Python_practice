class Result10th:
    def __init__(self, name, phone, email, year10, classname):
        self.name=name
        self.phone=phone
        self.email=email
        self.year10=year10
        self.classname=classname
    def display(self):
        print(self.name, self.phone, self.email,self.year10,self.classname)

class Result12th(Result10th):
    def __init__(self, name, phone, email, year10, classname,year12, percent12):
        super().__init__(name, phone, email, year10, classname)
        self.year12 = year12
        self.percent12 = percent12

class ResultBE(Result12th):
    def __init__(self, name, phone, email, year10, classname, year12, percent12, branch, university, be_percent):
        super().__init__(name, phone, email, year10, classname, year12, percent12)
        self.branch=branch
        self.university=university
        self.be_percent=be_percent
    def display_all(self):
        super().display()
        print(self.year12, self.percent12, self.branch, self.university, self.be_percent)
student1 = ResultBE("Nitesh", "9876543210", "nitesh@gmail.com", 2018, "SRS", 2020, 85,"BSC", "SJC", 8.5)
student1.display_all()