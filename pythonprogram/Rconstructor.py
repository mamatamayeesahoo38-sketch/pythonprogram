class Rectangle:
	def __init__(self):
		self.length= 5
		self.breadth= 7
	def show(self):
		print("rectangle length=",self.length)
		print("rectangle breadth=",self.breadth)
	def area(self):
		print("area of rectangle=",self.length * self.breadth)
	def perimeter(self):
		return 2*(self.length+self.breadth)
r = Rectangle()
r.show()
r.area()
print("perimeter of rectangle=",r.perimeter())