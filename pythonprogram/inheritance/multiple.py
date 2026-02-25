class A:
    def method1(self):
        print("Class A")

class B:
    def method2(self):
        print("Class B")

class C(A, B):  # inherits both A and B
    def method3(self):
        print("Class C")

obj = C()
obj.method1()
obj.method2()
obj.method3()