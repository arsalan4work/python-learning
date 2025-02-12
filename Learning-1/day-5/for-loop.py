# Loops are used for sequential traversal. For traversing list, string, tuples etc.
# A for loop in Python iterates over a sequence (such as a list, tuple, string, or range). It automatically takes one element at a time from the iterable and executes the block of code for that element.

# When to Use:
# Use a for loop when you have a collection of items or a known sequence to iterate over.

# Syntax Example:

# Iterating over a list
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# Key Points:
# The loop variable (here, fruit) automatically takes each value from the iterable.
# You don't need to manually initialize or update the loop variable.
# It is clear and concise when you know the number of iterations or items in advance.

############################################################################################################################
# In list
# veggies = ["Potato", "Ginger", "Tomato", "Cabbage", "Carrot"]

# for val in veggies:
#    print(val)

############################################################################################################################
# # In Tuple
# tup = (1,2,3,4,5)

# for val in tup:
#    print(val)
# else:
#    print("Loops end!")


# name = "Arsalan"

# for char in name:
#    if(char == 's'):
#       print("character found: ", char)
#       break
# else:
#    print("loops end!")

############################################################################################################################
# Practice
# Q1: Print the elements of the following list using loop: [1,4,9,16,36,49,64,81,100]

# nums = [1,4,9,16,36,49,64,81,100]

# for val in nums:
#    print(val)

############################################################################################################################
# Q2: Search for a number x in this tuple using loop: (1,4,9,16,25,36,49,64,81,100)

# nums = (1,4,9,16,25,36,49,64,81,100)

# x = ()

# for x in nums:
#    if(x == 25):
#       print("Found the value", x)
#       break
# else:
#    print("Error! Not found.")

############################################################################################################################
# Range in python
# Range func returns a sequence of numbers, starting from 0 by default, 
# and increment by 1 by default, and stops before a specified number. range(start?, stop, step?)

# for i in range(5): #range (stop)
#    print(i)

# print("Next/")
# for i in range(5,10): #range (start, stop)
#    print(i)

# print("Next/")
# for i in range(1,11,3): #range(start?, stop, step?)
#    print(i)


# Print Even numbers
# for i in range(1,101,2):
#    print(i)

# print("Next/")
# # Print odd numbers
# for i in range(2,101,2):
#    print(i)



############################################################################################################################
# What Is a List Comprehension?
# A list comprehension is a concise way to create lists in Python. Instead of writing multiple lines of code using a loop to build a list, you can use a single line that expresses the same logic. List comprehensions are essentially a shorter and more readable form of writing a loop that builds a list.

# How Do They Relate to Loops?
# When you use a loop to create a list, you typically:

# Start with an empty list.
# Loop through some sequence.
# Append a processed value from each iteration to the list.
# A list comprehension does all these steps in one line. It internally performs a loop over a sequence and constructs a new list from the results.

# Basic Structure
# A list comprehension has the following general form:

# python
# Copy
# Edit
# [expression for item in iterable]
# expression: This is the value or operation that you want to add to the list.
# for item in iterable: This part iterates over every item in an iterable (like a list, range, string, etc.).
###################################################################
# squares = []              # Start with an empty list
# for x in range(10):       # Loop over numbers 0 through 9
#     squares.append(x ** 2)  # Append the square of each number
# print(squares)
# # 
# squares = [x ** 2 for x in range(10)]
# print(squares)
