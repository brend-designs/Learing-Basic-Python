# Project Name: Lists
# Version: 1.0
# Author: Brendan Langenhoff (brend-designs)
# Description: Experimenting with lists (and iteration)

# Define an empty list
my_list = []

# Append values to list
my_list.append(1)
my_list.append(2)
my_list.append(3)

print(my_list[0])  # Prints 1st value in list
print(my_list[1])  # Prints 2nd value in list
print(my_list[2])  # Prints 3rd value in list

# Iterate and Print each value in the list
for x in my_list:
    print(x)

# Iterating through multiple lists to match values
names = ["John", "Eric", "George"]
ages = ["27", "19", "31"]
for i in range(len(names)):
    print(f"{names[i]} (Age: {ages[i]})")
