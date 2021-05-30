# Project Name: Basic String Operators
# Version: 1.0
# Author: Brendan Langenhoff (brend-designs)
# Description: Basic operations that can be performed with Strings.

# Define the string (which we will use operations on)
astring = "Hello world!"

print(f"The String is:  '{astring}'")

# len(str) counts the number of characters in the string
print(f"How long is this string? {len(astring)} characters")

# str.index(char) returns the index of where the character is within the string
print(f"At which index in the string, is the letter 'o'? {astring.index('o')}")

# str.count(char) counts the number of a specific character within the string
print(f"How many letter 'l''s are in this string? {astring.count('l')} ")

# str[startIndex:endIndex:step] get the characters between starting index and ending index, and how many characters we would be stepping (skipping). Remember: Indexing starts at 0
print(
    f"What characters are between the 3rd index and the 6th index? {astring[3:7:1]}")

# str.upper() to convert string to all uppercase characters.
print(f"What does this string look like in Uppercase? {astring.upper()}")

# str.lower() to convert string to all lowercase characters.
print(f"What does this string look like in Lowercase? {astring.lower()}")

# str.__contains__(chars) checks if our string contains the specified character(s)
print(
    f"Does our string contain a exclamation mark (!)? {astring.__contains__('!')}")

# str.startswith(chars) checks if a string starts with the specified characters or string.
print(f"Does our string start with 'Hello'? {astring.startswith('Hello')}")

# str.endswith(chars) checks if a string ends with the specified characters or string.
print(f"Does our string emd with 'world!'? {astring.endswith('world!')}")

# str.split(" ") will split a string where the specified character is found anywhere in the string, into a bunch of strings grouped together in list.
print(
    f"What if we split the string where there's a whitespace (space)? {astring.split(' ')}")
