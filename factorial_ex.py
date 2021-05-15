# Example 1
def fac(n):
	if n == 1:
		return 1
	else:
		return n * fac(n - 1)

print(fac(5))


# Example 2:
def factorial(n):

    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


# Driver Code
print(factorial(3))

list = [0, 1]
def fibonacci(n):
	for i in range(n-2):
		list.append(list[-1] + list[-2])
	return list


print(fibonacci(10))

def fib(n):
	a, b = 0, 1
	for _ in range(n):
		a, b = b, a + b
	return b

fib(10)