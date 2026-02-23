class Rectangle:
    def _init_(self, L, B):
        self.length = L
        self.breadth = B

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

print("Enter how many rectangle shapes:")
s = int(input())

rectangles = []

for i in range(s):
    print(f"Enter rectangle {i+1} length and breadth:")
    L = int(input("Length: "))
    B = int(input("Breadth: "))
    rectangles.append(Rectangle(L, B))

print("\n" + "-" * 60)
print(f"{'No':>5}{'Length':>10}{'Breadth':>10}{'Area':>10}{'Perimeter':>15}")
print("-" * 60)

for i, r in enumerate(rectangles, start=1):
    print(f"{i:>5}{r.length:>10}{r.breadth:>10}{r.area():>10}{r.perimeter():>15}")