class Square:
	def __init__(self,s):  
		self.side=s
	def show(self):
		print("square side=",self.side)
	def area(self):
		print("area of square=",self.side)
	def perimeter(self):
		return 4*(self.side)
print("enter square side")
L=[]
print("enter how many square shape")
s=int(input())
for i in range(s):
	print("enter square=",i+1," side")
	s=Square(int(input()))
	L.append(s)
for i in L:	
	i.show()
	i.area()
	print("perimeter of side=",i.perimeter())