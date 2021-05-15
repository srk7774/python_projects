#example 1
def divide42by(num):
	try:
		return 42 / num
	except:
		print('Error: Invalid argument.')
print(divide42by(2))
print(divide42by(3))
print(divide42by(0))
print(divide42by(5))

#example 2
def spam(divideBy):
	return 42 / divideBy


try:
	print(spam(2))
	print(spam(12))
	print(spam(0))
	print(spam(1))
except ZeroDivisionError:
	print('Error: Invalid argument.')

