class Rectangle:
    def __init__(self, L, B):   # constructor
        self.length = L
        self.breadth = B
    def show(self):
        return self.length, self.breadth
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
    rectangles.append(Rectangle(L,B))
print("\n{:<10}{:<10}{:<10}{:<10}{:<12}".format("Rectangle", "Length", "Breadth", "Area", "Perimeter"))
print("-" * 52)
for i, r in enumerate(rectangles, start=1):
    print("{:<10}{:<10}{:<10}{:<10}{:<12}".format(i,r.length,r.breadth,r.area(),r.perimeter()))