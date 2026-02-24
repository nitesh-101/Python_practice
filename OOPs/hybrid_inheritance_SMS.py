class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll
class Academic:
    def __init__(self, course=None, cgpa=None):
        self.course = course
        self.cgpa = cgpa
class Sports:
    def __init__(self, sport_name=None, level=None):
        self.sport_name = sport_name
        self.level = level
class AllRounderStudent(Student, Academic, Sports):
    def __init__(self, name, age, roll, is_academic=False, is_sports=False, course=None, cgpa=None, sport_name=None, level=None):
        super().__init__(name, age, roll)
        self.is_academic = is_academic
        self.is_sports = is_sports

        if self.is_academic:
            Academic.__init__(self, course, cgpa)
        if self.is_sports:
            Sports.__init__(self, sport_name, level)
    def display(self):
        print(self.name, self.age, self.roll)

        if self.is_academic:
            print(self.course, self.cgpa)
        if self.is_sports:
            print(self.sport_name, self.level)
s1 = AllRounderStudent('Nitesh', 24, 101, is_sports=True, course="MCA", cgpa=9.10, sport_name="Football", level="State")
s1.display()