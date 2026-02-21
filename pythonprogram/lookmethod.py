class Demo:
	def show(self):
		print("instance show method")
	@classmethod
	def look(cls):
		print("class look method")
	@staticmethod
	def disp():
		print("disp static method")
d=Demo()
d.show()
d.look()
d.disp()
Demo.look()
Demo.disp()