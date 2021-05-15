from sympy import *
print(isprime(11))
print(fibonacci(10))

print(primepi(100))

n = int(input())
if n < 2:
	print("Primes are defined for positive numbers only")
elif n == 1:
	print("1 is neither prime nor composite")
elif n == 2 or n == 3:
	print("Prime!!")
else:
	for i in range(2, n):
		if n % i == 0:
			print("Not a Prime Number!!")
			break
	else:
		print("Prime Number!!")

import random
random.randint(1, 10)
random.uniform(1, 10)

random.gauss(1, 1)
random
