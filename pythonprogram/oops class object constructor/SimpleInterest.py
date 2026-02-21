class SimpleInterest:
	def __init__(self ,p,t,r):
		self.principle=p
		self.time=t
		self.rate=r
	def show(self):
		print("principle=",self.principle)
		print("time=",self.time)
		print("rateofinterest=",self.rate)
	def SI(self):
		print("simpleinterest=",self.principle*self.time*self.rate/100)

s=SimpleInterest(5000,6,2)
s.show()
s.SI()

s1=SimpleInterest(6000,4,2)
s1.show()
s1.SI()
