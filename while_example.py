spam = 0
while spam < 5:
	print('Hello world')
	spam = spam + 1

# example
name = ''
while name != 'your name':
	print('Please type your name')
	name = input()
print('thank you')

# example
name = ''
while True:
	print('Please type your name')
	name = input()
	if name == 'your name':
		break
print('thank you')

# Example
spam = 0
while spam < 5:
	spam = spam + 1
	if spam == 3:
		continue
	print('spam is ' + str(spam))
