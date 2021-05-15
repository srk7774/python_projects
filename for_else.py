# Python 3.x program to check if an array consists
# of even number
'''


'''
def contains_even_number(l):
	for ele in l:
		if ele % 2 == 0:
			print ("list contains an even number")
			break

	# This else executes only if break is NEVER
	# reached and loop terminated after all iterations.
	else:
		print ("list does not contain an even number")


contains_even_number([1, 2, 5])

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break


# Next example
for letter in 'Python':  # First Example
	if letter == 'h':
		break
	print ('Current Letter :', letter)

# Third Example
var = 10
while var > 0:
   print ('Current variable value :', var)
   var = var -1
   if var == 5:
      break  #break always terminates the remaining executions

print ("Good bye!")

