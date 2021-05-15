from abc import ABC, abstractmethod
class AbstractDemo(ABC):
	@abstractmethod
	def display(self):
		None

class Demo(AbstractDemo):
	def display(self):
		print('Abstract Method')

obj = AbstractDemo() #This gives error
obj = Demo()
obj.display()

# This gives error becuase concrete class has not got all methods
from abc import ABC, abstractmethod
class AbstractDemo(ABC):
	@abstractmethod
	def display(self):
		None
	@abstractmethod
	def show(self):
		None

class Demo(AbstractDemo):
	def display(self):
		print('Abstract Method')

obj = AbstractDemo() #This gives error
obj = Demo()
obj.display()

# This gives error becuase concrete class has not got all methods
from abc import ABC, abstractmethod
class AbstractDemo(ABC):
	@abstractmethod
	def display(self):
		None
	@abstractmethod
	def show(self):
		None

class Demo(AbstractDemo):
	def display(self):
		print('Abstract Method')
	def show(self):
		print('show method')

obj = Demo()
obj.display()