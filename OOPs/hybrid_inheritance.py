class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll=roll
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject=subject
class Academic:
    def __init__(self, subject, marks):
        self.subject=subject
        self.marks=marks
class Sports:
    def __init__(self, sport_name, level):
        self.sport_name=sport_name
        self.level=level
class AllRounderStudent(Student, Academic, Sports):
    def __init__(self, name, age, roll_no, subject, marks, sport_name, level):
        Student.__init__(self, name, age, roll_no)
        Academic.__init__(self, subject, marks)
        Sports.__init__(self, sport_name, level)
    def display(self):
        print(self.name, self.age, self.roll, self.subject, self.marks, self.sport_name, self.level)
s1 = AllRounderStudent("Nitesh", 24, 101, "Python", 85, "Football", "State")
s1.display()