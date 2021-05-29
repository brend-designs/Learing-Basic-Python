# Project Name: Basic Operators
# Version: 1.0
# Author: Brendan Langenhoff (brend-designs)
# Description: Basic Operators such as Arithmetic Operators (math), and using operators with Strings and Lists.

# 1. Arithmetic Operators (Addition, Subtraction, Multiplication + Division)
# ================================================================
number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3  # Remainder of 11 divided by 3
print(remainder)

squared = 7 ** 2  # 7 squared (7 x 7)
cubed = 2 ** 3  # 3 cubed (3 x 3 x 3)
print(squared)
print(cubed)
# ================================================================


# 2. Using Operators with Strings
# ================================================================
helloworld = "hello" + " " + "world"
print(helloworld)

lotsofhellos = "hello" * 10  # 10x "hello"
print(lotsofhellos)
# ================================================================


# 3. Using Operators with Lists
# ================================================================
even_numbers = [2, 4, 6, 8, 10]
odd_numbers = [1, 3, 5, 7, 9]
all_numbers = even_numbers + odd_numbers
print(all_numbers)

# Just like strings, Python supports forming new lists with a repeating
# sequence using the multiplication operator:
print([1, 2, 3] * 3)
# ================================================================
