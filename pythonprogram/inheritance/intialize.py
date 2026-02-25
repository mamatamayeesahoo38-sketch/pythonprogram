class A:
	def setA(self):
		self.x=10
	def dispA(self):
		print(self.x)
class B(A):
	def setB(self):
		self.y=20
	def dispB(self):
		print(self.y)
ob=B()
ob.setA()
ob.dispA()
ob.setB()
ob.dispB()
