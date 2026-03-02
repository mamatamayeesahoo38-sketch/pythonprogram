class Rectangle:
	def __init__(self,L,B):   
		self.length=L
		self.breadth=B
	def show(self):
		print("rectangle lenegth=",self.length)
		print("rectangle breadth=",self.breadth)
	def area(self):
		print("area of rectangle=",self.length*self.breadth)
	def perimeter(self):
		return 2*(self.length+self.breadth)
print("enter rectangle length and breadth ")
L=[]
print("enter how many rectangle shape")
s=int(input())
for i in range(s):
	print("enter rectangle ",i+1," length and breadth")
	r=Rectangle(int(input()),int(input()))
	L.append(r)
for i in L:	
	i.show()
	i.area()
	print("perimeter of rectangle=",i.perimeter())