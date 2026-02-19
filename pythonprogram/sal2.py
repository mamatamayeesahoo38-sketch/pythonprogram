print("enter monthly salary")
Sal=float(input())
print("enter salary of da")
da=float(input())
print("enter salary of HR")
HR=float(input())
print("enter tax")
tax=float(input())
da=Sal*0.2
HR=Sal*0.15
tax=Sal*0.1
totalm=Sal+da+HR-tax
totala=Sal*12
print("basic salary=",Sal)
print("salary of da=",da)
print("salary of HR=",HR)
print("tax from salary=",tax)
print("monthly salary=",totalm)
print("annual salary=",totala)
