# Project Name: Classes & Objects
# Version: 1.0
# Author: Brendan Langenhoff (brend-designs)
# Description: Encapsulating variables and functions into a single entity (objects) and using classes for objects to get their variables and functions from.

# A very basic class
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


# Assigning a class to an object
my_object_x = MyClass()

# Accessing variable in the object
print(my_object_x.variable)

# Assigning a second object using the class
my_object_y = MyClass()

# Re-assigning or changing a variable within the object
my_object_y.variable = "yooo"

print(my_object_y.variable)

# Accessing a function inside an object
my_object_y.function()
