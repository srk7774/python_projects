class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))


# Example 2
# it is clearly seen that self and obj is refering to the same object

class check:
    def __init__(self):
        print("Address of self = ", id(self))


obj = check()
print("Address of class object = ", id(obj))


# this code is Contributed by Samyak Jain

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print("Model is", self.model)
        print("Color is", self.color)


c1 = Car("Audi", "Blue")
c2 = Car("BmW", "red")

c1.show()
