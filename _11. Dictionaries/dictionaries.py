# Project Name: Dictionaries
# Version: 1.0
# Author: Brendan Langenhoff (brend-designs)
# Description: Using the Dictionary data type which is similar to arrays, but works with keys and values instead of indexes.

# Define an empty Dictionary
phonebook = {}

# Storing values using specific keys, so we may retrieve them later using these keys
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781

# Print all keys and values of defined Dictionary
print(phonebook)


# Iterating over Dictionaries
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))


# Removing a value from a Dictionary
del phonebook["John"]  # Remove the value which has the key "John"
# Removing a value can also be done via the .pop function:
# phonebook.pop("John")
print(phonebook)  # Re-print after removing a value
