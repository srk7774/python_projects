class Student:
	rno = 123
	name = 'abc'
	branch = 'cse'

#rno, name, branch are instance variables

	def read(self):
		print('Reading...')
	def write(self):
		print('writing...')

s1 = Student()
s2 = Student()

s1.rno
s1.name
s1.branch
Student.rno
s1.read()