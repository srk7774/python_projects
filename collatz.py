num = int(input('Enter a number:',))

def collatz(num):
	while num != 1:
		print(num, end = ' ')
		if num % 2 == 0:
			num =  num // 2
		else:
			num =  3*num + 1
	print(num)

collatz(num)

class Abc:
	pass