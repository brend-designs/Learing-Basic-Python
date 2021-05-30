# Project Name: Loops
# Version: 1.0
# Author: Brendan Langenhoff (brend-designs)
# Description: Experimenting with the two types of loops in Python, "for" and "while".


# For loops - Iterates over a given sequence.
primes = [2, 3, 5, 7]
for prime in primes:  # For each value in list, then do x
    print(prime)

# Prints out the numbers in the range of 5 (0, 1, 2, 3, 4)
for x in range(5):
    print(x)

# Prints out the numbers between the range of 3 and 6 (3,4,5)
for x in range(3, 6):
    print(x)

# Prints out the numbers between the range of 3 and 8, whilst stepping (skipping 2) numbers (3, 5, 7)
for x in range(3, 8, 2):
    print(x)


# While loops - Repeats as long as certain boolean condition is met.
count = 0
while True:
    print(count)
    count += 1


# "break" and "continue" statements.

# Prints out numbers if count is less than 5, then break out of the loop if count is greater than or equal to 5.
count = 0
while True:
    print(count)
    count += 1
    if (count >= 5):
        break

# Prints out only odd numbers (1, 3, 5, 7, 9)
for x in range(10):
    if x % 2 == 0:  # Checks if 'x' is even
        continue
    print(x)


# Using the "else" clause in loops

# Prints out 0, 1, 2, 3, 4 and then once count reachs 5, it will print "'count' value reached 5"
count = 0
while(count < 5):
    print(count)
    count += 1
else:
    print("'count' value has reached 5")

# Prints out 1,2,3,4 and then breaks the loop once the value of 'i' has a remainder when being divided by 5, and prints message.
for i in range(1, 10):
    if i % 5 == 0:
        break
    print(i)
else:
    print("This is not printed because for loop is terminated because of break, not due to fail in condition")
