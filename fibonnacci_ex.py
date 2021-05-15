# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

#example 2
def fibonacci(a, b, n):
	count = 0
	if n <= 0:
		print("Enter a positive number")
	elif n == 1:
		print(a)
	else:
		for i in range(n):
			print(a, end = ' ')
			c = a + b
			a = b
			b = c

fibonacci(1, 1, 10)


#2 Python program to display the Fibonacci sequence

def fib_to(n):
	fibs = [0, 1]
	for i in range(2, n + 1):
		fibs.append(fibs[-1] + fibs[-2])
	return fibs


fib_to(10)

# example 3
import functools

@functools.lru_cache(None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

fib(10)


# example 4
def fib(n, computed={0: 0, 1: 1}):
	if n not in computed:
		computed[n] = fib(n - 1, computed) + fib(n - 2, computed)
	return computed[n]


fib(400)

 #example 5 factorial of given number

def factorial(n):

    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


# Driver Code
num = 5
print ("Factorial of", num, "is",
      factorial(num))


# Example 6
def fib(n):
	a, b = 0, 1
	for _ in range(n):
		a, b = b, a + b
	return b


print(fib(10))

# python program to check if x is a perfect square
import math


# A utility function that returns true if x is perfect square
def isPerfectSquare(x):
	s = int(math.sqrt(x))
	return s * s == x


# Returns true if n is a Fibinacci Number, else false
def isFibonacci(n):
	# n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both
	# is a perferct square
	return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)


# A utility function to test above functions
for i in range(1, 11):
	if (isFibonacci(i) == True):
		print
		i, "is a Fibonacci Number"
	else:
		print
		i, "is a not Fibonacci Number "


