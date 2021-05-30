# Project Name: Conditions
# Version: 1.0
# Author: Brendan Langenhoff (brend-designs)
# Description: Boolean logic to evaluate conditions.

x = 2
print(x == 2)  # Prints out True (Logic: is 'x' equal to 2?)
print(x == 3)  # Prints out False (Logic: is 'x' equal to 3?)
print(x < 3)  # Prints out False (Logic: is 'x' less than 3?)
print(x > 1)  # Prints out True (Logic: is 'x' greater than 1?)
print(x >= 2)  # Prints out True (Logic: is 'x' greater than OR equal to 2?)
print(x <= 3)  # Prints out True (Logic: is 'x' less than OR equal to 3?)
print(x != 2)  # Prints out False (Logic: is x is not equal to 2?)


name = "John"
age = 23

# Returns True (Logic: is their name 'John' AND is there age equal to 23?)
if name == "John" and age == 3:
    print("Your name is John, and you are also 23 years old.")

# Returns True (Logic: is their name 'John' OR is there name 'Rick'?)
if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# Return True (Logic: is their name in a iterable object (such as a list) which contains 'John' and 'Rick'?)
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")


# Example of 'if, else if then else' statement
statement = False
another_statement = True

if statement is True:
    # do something
    pass
elif another_statement is True:  # else if statement
    # do something else
    pass
else:
    # do another thing
    pass


# Example of "is" operator
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # Prints out True (Logic: Does x match the values of y? (Variable wise))
# Prints out False (Logic: Is y the instance of x? (Not comparing values of the variables))
print(x is y)


# Example of "not" operator to invert a boolean expression.
print(not False)  # Prints out True
print((not False) == (False))  # Prints out true
