class MOverload:
	def display(self, a=None, b=None):
		print(a, b)

obj = MOverload()
obj.display()
obj.display(10)