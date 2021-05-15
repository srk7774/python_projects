# example 1
i = 1
while i < 8:
	print(i)
	i = i + 1


# example 2
i = 1
while i < 6:
	print(i)
	i = i + 1
	if i == 3:
		break

# example 3
i = 1
while i < 6:
	print(i)
	i = i + 1
	if i == 4:
		break

#example 4
while True:
	number = float(input("Enter a number"))
	if number < 0:
		break
	print("You entered: ", number)

#example 5
for i in range(1, 51, 3):
	if i == 7:
		continue
	else:
	print(i, end=' ')

#example 6
for i in range(1, 51, 3):
	if i == 7:
		break
	else:
		print(i, end=' ')

#example 7
n = int(input("Enter n value"))
i = 0
while i <= n:
	print(i)
	i = i + 1

#example 8
i = 1
while i <= 10:
	if i == 5:
		pass
	print(i)
	i = i + 1

i = 1
list = []

while i <= 10:
	list.append(i)
	i += 1
print(list)

list1 = []
for i in range(1, 51, 3):
	list1.append(i)


import matplotlib.pyplot as plt
import numpy as np

cnums = np.arange(5) + 1j * np.arange(6,11)
X = [x.real for x in cnums]
Y = [x.imag for x in cnums]
plt.scatter(X,Y, color='red')
plt.show()

