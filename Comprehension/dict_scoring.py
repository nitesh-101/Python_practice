students={"Rahul": 75, "Anita": 45, "Riya": 82, "Amit": 59}
d= {name: marks for name, marks in students.items() if marks>=60}
print(d)