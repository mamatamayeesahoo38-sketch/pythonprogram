class A:
    def method1(self):
        print("A")

class B(A):
    def method2(self):
        print("B")

class C:
    def method3(self):
        print("C")

class D(B, C):  # hybrid
    def method4(self):
        print("D")

obj = D()
obj.method1()
obj.method2()
obj.method3()
obj.method4()