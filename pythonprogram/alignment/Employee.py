class Employee:
    def __init__(self, name, emp_id, basic):
        self.name = name
        self.emp_id = emp_id
        self.basic = basic
        self.da = 0.10 * basic       # 10% DA
        self.hra = 0.15 * basic      # 15% HRA
        self.tax = 0.05 * basic      # 5% Tax
        self.total = basic + self.da + self.hra - self.tax

print("Enter how many employees:")
n = int(input())

employees = []

for i in range(n):
    print(f"\nEnter details for Employee {i+1}")
    name = input("Name: ")
    emp_id = input("ID: ")
    basic = float(input("Basic Salary: "))
    
    employees.append(Employee(name, emp_id, basic))

# Table Header
print("\n{:<12}{:<10}{:>12}{:>10}{:>10}{:>10}{:>12}".format(
    "Name","ID","Basic","DA","HRA","Tax","Total"))

print("-" * 76)

# Table Data
for e in employees:
    print("{:<12}{:<10}{:>12.2f}{:>10.2f}{:>10.2f}{:>10.2f}{:>12.2f}".format(
        e.name, e.emp_id, e.basic, e.da, e.hra, e.tax, e.total))