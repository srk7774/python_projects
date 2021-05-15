# Program to check if a number is prime or not

num = -4

# To take input from the user
#num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num == 1:
    print(1, "is neither prime nor composite")
elif num < 1:
    print(num, "is negative")

elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")
            break

