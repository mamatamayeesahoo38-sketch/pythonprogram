class Square:
	def __init__(self):
		self.side = 5
	def show(self):
		print("square side =",self.side)
		
	def area(self):
		print("area of square =",self.side * self.side)
	def perimeter(self):
		return 4*(self.side)
s = Square()
s.show()
s.area()
print("perimeter of square=",s.perimeter())