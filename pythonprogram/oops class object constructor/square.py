class square:
	def __init__(self ,side):
		self.side=side
	def show(self):
		print("side=",self.side)
	def area(self):
		print("area of square=",self.side*self.side)
	def perimeter(self):
		return 4*self.side
s=square(5)
s.show()
s.area()
print("perimeter of square=",s.perimeter())