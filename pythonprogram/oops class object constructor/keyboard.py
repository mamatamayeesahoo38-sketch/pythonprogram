class Rectangle:
	def __init__(self,L,B):
		self.length=L
		self.bredth=B
	def show(self):
		print("Rectangle length=",self.length)
		print("Rectangle breadth=",self.breadth)
	def area(self):
		print("area of rectangle=",self.length*self.breadth)
	def perimeter(self):
		return 2*(self.length+self.bfreadth)
print("enter rectangle length and bredth")
r=Rectangle(int(input()),int(input()))
r.show()
r.area()
print("perimeter of rectangle=",r.perimeter())