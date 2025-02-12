# Q1: Print numbers from 1 to 100 using for & range.
# for i in range(1,101):
#    print(i)


# Q2: Print numbers from 100 to 1 using for & range.

# for i in range(100, 0, -1):
#     print(i)


# Q3: Print the multiplication table of a number n.

# n = int(input("Enter a number: "))
# for i in range(1,11):
#       print(n*i)


# Q4: Write a program to find sum of first n numbers.(using while)
# n = int(input("Enter a number: "))
# sum = 0
# i = 1

# while i <= n:
#    sum += i
#    i += 1

# print("total sum = ",sum)

# Q5: Write a program to find the factorial of first n numbers.(using for)

# n = int(input("Choose a number between 1-9: "))
# fact = 1

# for i in range (1, n+1):
#    fact *= i

# print("Factorial = ",fact)

# Write a program that uses nested loops to print the multiplication table for numbers 1 to 5. 
# For example, the output should show lines like 2 x 3 = 6.
# Hint: Use an outer loop for the first number and an inner loop for the second number.

# for i in range (1,5):
#    for i in range(1,10):
#       i * i
#       i += 1
#       print(i)

# Create a dictionary with at least three key-value pairs (for example, a dictionary of student names and their grades). 
# Write a program that uses a loop to iterate over the dictionary and print each key with its corresponding value.
# Hint: Use the .items() method to loop through key-value pairs.

# student1 = {
#    "name": "Arsalan",
#    "age": 20,
#    "grades" :{
#       "computer": 73,
#       "english": 81,
#       "physics": 94,
#       "chemistry": 88,
#    },
# }

# for key, value in student1.items():
#    print(key, ":", value)

# print("Next/")
# for key, value in student1["grades"].items():
#    print(key, ":", value)


# Given a list of strings (e.g., fruits = ["apple", "banana", "cherry"]), write a program that uses a loop to print each fruit in the list.
# (Using for loop)

fruits = ["apple", "banana", "cherry"]

for name in fruits:
   print(name)