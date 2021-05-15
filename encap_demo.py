class Encap:
	a = 10
	def display(self):
		print("welcome")

obj = Encap()
print(obj.a)
obj.display()

#next example
class Encap:
	__a = 10   #private variable
	def display(self):
		print("welcome")
		print(self.__a)

obj = Encap()
obj.display()