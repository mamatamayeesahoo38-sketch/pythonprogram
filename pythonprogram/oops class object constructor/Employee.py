class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def show(self):
        print("employee id =", self.emp_id)
        print("employee name =", self.name)
        print("employee salary =", self.salary)

    def da(self):
        return 0.10 * self.salary

    def hra(self):
        return 0.15 * self.salary

    def totalsalary(self):
        return self.salary + self.da() + self.hra()


print("enter how many employee work")
n = int(input())

L = []

for i in range(n):
    print("enter employee", i + 1, "emp_id, name, salary")
    emp = Employee(int(input()), input(), int(input()))
    L.append(emp)

for i in L:
    i.show()
    print("totalsalary =", i.totalsalary())