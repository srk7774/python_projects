import random

random.randint(1, 6)

l = [10, 20, 30, 40]
random.choices(l, k=2)

random.randrange(10, 15, 1)

random.random()
random.shuffle(l)
random.uniform(1, 100)

random.triangular(1, 10, 5)

random.triangular(1, 10)

n = 10

def fib(n):
    fib_list = [0, 1]
    for i in range(n-2):
        fib_list.append(fib_list[-1]+fib_list[-2])
    return fib_list

fib(10)