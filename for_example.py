print('My name is')
for i in range(5):
	print('Jimmy Five times' + str(i))

total = 0
for num in range(101):
	total = total + num
print(total)

i = 0
while i < 5:
	print("jimmy five times" + str(i))
	i = i + 1

#Example
for i in range(5):
	number = float(input("Enter a number"))
	if number < 0:
		continue
	print(number)

#Example
languages = ["Python", "Java", "Swift", "C", "C++"]

for language in languages:
	if language == "Swift" or language == "C++":
		continue
	print(language)
