class A:
	def setA(self):
		self.x=10
	def dispA(self):
		print(self.x)
class B(A):
	pass
ob=B()
ob.setA()
ob.dispA()

