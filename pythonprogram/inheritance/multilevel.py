class GrandParent:
    def gp(self):
        print("GrandParent")

class Parent(GrandParent):
    def p(self):
        print("Parent")

class Child(Parent):
    def c(self):
        print("Child")

obj = Child()
obj.gp()
obj.p()
obj.c()