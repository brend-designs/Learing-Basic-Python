# Project Name: Loops
# Version: 1.0
# Author: Brendan Langenhoff (brend-designs)
# Description: Using functions as a convenient way to divide code - allowing us to order our code, make it more readable, reuse it and save some more time.

# block_head:
#     1st block line
#     2nd block line
#     ....

# Simple function without parsing any arguments
def my_function():
    print("Hello from my Function!")


my_function()

# Receiving arguments (variables pased from the caller to the function


def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" %
          (username, greeting))


my_function_with_args("Brendan", "hello!")

# Returning a value to the caller - using the keyword 'return'


def sum_two_numbers(a, b):
    return a + b


print(sum_two_numbers(5, 5))
