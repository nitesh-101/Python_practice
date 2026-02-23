class Tenth():
    name="SRS"
    location="Darjeeling"
    def __init__(self, name, location):
        self.name=name
        self.location=location
    @classmethod
    def details(cls):
        print(cls.name, cls.location)

class Twelveth(Tenth):
    def __init__(self, name, location, twname, twmarks):
        super().__init__(name, location)
        self.twname=twname
        self.twmarks=twmarks
    def display(self):
        print(self.twname, self.twmarks)
a1 = Twelveth("SJC", "Sikkim", "Nitesh", 90)
Twelveth.details()
a1.display()