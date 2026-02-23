class sal:
    def __init__(self, emp_id, name, salary):   
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def show(self):
        return self.emp_id, self.name, self.salary

    def da(self):
        return 0.10 * self.salary   

    def hra(self):
        return 0.15 * self.salary  

    def total_salary(self):
        return self.salary + self.da() + self.hra()


print("Enter how many employees:")
n = int(input())

employees = []

for i in range(n):
    print(f"Enter employee {i+1} details:")
    emp_id = int(input("Employee ID: "))
    name = input("Name: ")
    salary = float(input("Basic Salary: "))
    employees.append(sal(emp_id, name, salary))

print("\n{:<8}{:<15}{:<10}{:<10}{:<10}{:<12}".format(
    "ID", "Name", "Salary", "DA", "HRA", "Total"))
print("-" * 65)

for e in employees:
    print("{:<8}{:<15}{:<10.2f}{:<10.2f}{:<10.2f}{:<12.2f}".format(
        e.emp_id,
        e.name,
        e.salary,
        e.da(),
        e.hra(),
        e.total_salary()
    ))