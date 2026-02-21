class Rectangle:
	def __init__(self):
		print("enter rectangle length and breadth")
		self.length=int(input())
		self.breadth=int(input())
	def show(self):
		print("rectangle length=",self.length)
		print("rectangle bredath=",self.breadth)
	def area(self):
		print("area of rectangle =",self.length*self.bredth)
	def perimeter(self):
		return 2*(self.length+self.bredth)
r=Rectangle()
r.show()
r.area()
print("perimeter of rectangle=",r.perimeter())
r1=Rectangle()
r1.show()
r1.area()
print("perimeter of rectangle=",r1.perimeter())