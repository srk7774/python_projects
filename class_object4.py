class Dog:
	def add_one(self, x):
		return x + 1

	def __init__(self, name):
		self.name = name

	def bark(self):
		print('bark')

a = Dog("Tim")
b = Dog("Bill")
print(a.name)
print(b.name)

#example 2
class Dog:
	def get_name(self):
		return self.name

	def __init__(self, name):
		self.name = name

a = Dog("Tim")
b = Dog("Bill")
print(a.get_name())
print(b.get_name())