from abc import ABC,abstractmethod
class Animal(ABC):
	@abstractmethod
	def sound(self):
		pass
	def sleep(self):
		print("sleeping...")
class Dog(Animal):
	def sound(self):
		print("Bark")
class Cat(Animal):
	def sound(self):
		print("Meow")
	
dog=Dog()
dog.sound()
dog.sleep()

cat=Cat()
cat.sleep()