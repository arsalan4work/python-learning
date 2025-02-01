# While Loop
# Definition:
# A while loop repeatedly executes a block of code as long as a given condition remains True. It’s controlled by a condition rather than by iterating over a collection.

# When to Use:
# Use a while loop when the number of iterations is not known in advance and you want to continue looping until a specific condition changes.

# Syntax Example:

# # Using a while loop to print numbers 1 to 5
# i = 1
# while i <= 5:
#     print(i)
#     i += 1  # Manual update of the loop variable is necessary!

# Key Points:
# You must initialize a loop variable before the loop starts.
# The loop condition is checked at the beginning of each iteration.
# You must update the loop variable inside the loop; otherwise, it could result in an infinite loop.
# It's more flexible for cases where you don't know exactly how many times you'll need to loop.

############################################################################################################################
# i = 1
# while i <= 100:
#    print("Hello Arsalan, Welcome!")
#    i += 1

############################################################################################################################
# Practice Questions
############################################################################################################################
#Q1 Print numbers from 1 to 100
# i = 1
# while i <= 100:
#    print(i)
#    i += 1

############################################################################################################################
#Q2 Print numbers from 100 to 1
# i = 100
# while i >= 1:
#    print(i)
#    i -= 1

############################################################################################################################
#Q3 Print the multiplication table of a number n.
# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#    print(n*i)
#    i += 1

############################################################################################################################
#Q4 Print the elements of the following list using loop: [1,4,9,16,25,36,49,64,81,100].
# nums = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(nums):
#    print(nums[idx])
#    idx += 1
# # Traverse (Travel one by one)
# heros = ["Ironman", "Thor", "Spuerman", "Batman", "Spiderman"]
# i = 0
# while i < len(heros):
#    print(heros[i])
#    i += 1

############################################################################################################################
#Q5 Search for a number x in this tuple using loop: (1,4,9,16,25,39,49,64,81,100).

# nums = (1,4,9,16,25,39,49,64,81,100)

# x = 39

# i = 0
# while i < len(nums):
#    if(nums[i] == x):
#       print("Found at index: ", i)
#    i += 1

# Break used to terminate the loop

# i = 0
# while i <= 5:
#    print(i)
#    if(i == 3):
#       break
#    i += 1

# print("Loop end")

# Continue terminates execution in the current iteration & continue executionof the loop with the next iteration

# i = 0 
# while i <= 10:
#    if(i%2 == 0):
#       i += 1
#       continue
#    print(i)
#    i += 1