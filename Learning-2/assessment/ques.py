# Short Answer Questions (30 Marks)
# (5 Marks each)
# Q1: Explain the difference between a list and a tuple in Python.
# A: In Python both list and Tuple are container to store a set of values of any data type. 
# List can be modified(mutable) and Tuple can not be modified(immutable). 
# List can be slower due to its mutable nature and Tuple can be fast due to its fixed size nature.
 
# Q2: What is a dictionary in Python? Provide an example.
# A: Dictionaries is a built-in data type used to store collections of data as key-value pairs.
# Each key is unique and associated with a value, Keys must be unique but values of 2 keys or more can be same.
# Example: 
# car = {
#     "brand": "Toyota",
#     "model": "Corolla",
#     "year": 2024
# }
# print(car["brand"])

# Q3: Describe what a lambda function is and provide a simple example.
# A: A lambda function in Python is a function defined using the lambda keyword. 
# Unlike regular functions defined with the def keyword, a lambda function is usually a one-liner 
# and is often used when you need a simple function for a short period.
# Eample: 
# num = lambda x,y: x+y
# result = num(3,5)
# print(result)

# Q4: What are list comprehensions? Write a list comprehension to create a list of squares of numbers from 1 to 10.
# A: List comprehensions is a concise way to create lists by applying an 
# expression to each item in an existing iterable (such as a list, tuple, or range),
# to write more compact and readable code compared to using traditional for loops.
# Example: 
# squares = [x**2 for x in range(1, 11)]
# print(squares)


# Q5: Explain the concept of exception handling in Python. Provide a code example.
# A: Exception handling allows us to handle runtime errors (exceptions) in a controlled way, 
# without crashing the program. It lets you detect errors, respond to them, and continue executing the program without interruption.
# try:
#     num1 = int(input("Enter the number 1: "))
#     num2 = int(input("Enter the number 2: "))
#     result = num1 / num2
    
# except ZeroDivisionError:
#     # Handling division by zero error
#     print("Error: Cannot divide by zero!")
    
# except ValueError:
#     # Handling invalid input type (non-integer)
#     print("Error: Please enter valid integers!")
# except Exception as e:
#     # When the exception is handled, the code flow continues without program interruption
#     print(f"Error! {e}")
    
# else:
#     # Code runs if no exception occurred
#     print(f"The result of the division is: {result}")
    
# finally:
#     # Code that always runs finally after successfull execution
#     print("Execution completed.")
