class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks


print("how many students")
n = int(input())

students = []

for i in range(n):
    print(f"\nEnter details for Student {i+1}")
    roll = int(input("roll: "))
    name = input("name: ")
    marks = int(input("marks: "))
    
    students.append(Student(roll, name, marks))

# Table Header
print("\n{:<12}{:<15}{:>10}".format("Roll", "Name", "Marks"))
print("-" * 37)

# Table Data
for s in students:
    print("{:<12}{:<15}{:>10}".format(s.roll, s.name, s.marks))