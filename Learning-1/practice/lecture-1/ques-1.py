# Write a program that takes an integer input from the user and prints its type. Then, take a floating-point 
# input and print its type. Explain why both inputs are treated as strings initially.

intVal = input("Enter a number: ")
print(type(intVal))
floatVal = input("Enter the matric percentage: ")
print(type(floatVal))

# In python the input() func always stored in a string, enev if the user enters a number. I explicitly convert it into an integar
# int() or a floating value float() to change its type

intVal = int(input("Enter a number: "))
print(type(intVal))
floatVal = float(input("Enter the matric percentage: "))
print(type(floatVal))