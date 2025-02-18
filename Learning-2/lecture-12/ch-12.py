# The walrus operator (:=), introduced in Python 3.8, allows you to assign values to
# variables as part of an expression. This operator, named for its resemblance to the eyes
# and tusks of a walrus, is officially called the "assignment expression."
# Using walrus operator
# if (n := len([1, 2, 3, 4, 5])) > 3:
#    print(f"List is too long ({n} elements, expected <= 3)")
# # Output: List is too long (5 elements, expected <= 3)

#########################################################################################################################

# TYPES DEFINITIONS IN PYTHON
# Type hints are added using the colon (:) syntax for variables and the -> syntax for
# function return types.

# Variable type hint
# age: int = 25
# # Function type hints
# def greeting(name: str) -> str:
# return f"Hello, {name}!"
# # Usage
# print(greeting("Alice")) # Output: Hello, Alice!


# ADVANCED TYPE HINTS
# Python's typing module provides more advanced type hints, such as List, Tuple, Dict,
# and Union.
# You can import List, Tuple and Dict types from the typing module like this:
# from typing import List, Tuple, Dict, Union
# 49
# The syntax of types looks something like this:


# from typing import List, Tuple, Dict, Union

# # List of integers
# numbers: List[int] = [1, 2, 3, 4, 5]

# # Tuple of a string and an integer
# person: Tuple[str, int] = ("Alice", 30)

# # Dictionary with string keys and integer values
# scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# # Union type for variables that can hold multiple types
# identifier: Union[int, str] = "ID1

#########################################################################################################################

# MATCH CASE
# Python 3.10 introduced the match statement, which is similar to the switch statement
# found in other programming languages.
# The basic syntax of the match statement involves matching a variable against several
# cases using the case keyword.

# def http_status(status):
#    match status:
#      case 200:
#          return "OK"
#      case 404:
#          return "Not Found"
#      case 500:
#        return "Internal Server Error"
#      case _:
#         return "Unknown status"
# # Usage
# print(http_status(200)) # Output: OK
# print(http_status(404)) # Output: Not Found
# print(http_status(500)) # Output: Internal Server Error
# print(http_status(403)) # Output: Unknown status

#########################################################################################################################

# DICTIONARY MERGE & UPDATE OPERATORS
# New operators | and |= allow for merging and updating dictionaries.

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# merged = dict1 | dict2
# print(merged) # Output: {'a': 1, 'b': 3, 'c': 4}

# You can now use multiple context managers in a single with statement more cleanly
# using the parenthesised context manager
# with (
#    open('file1.txt') as f1,
#    open('file2.txt') as f2
# ):
# Process files

#########################################################################################################################
# EXCEPTION HANDLING IN PYTHON
# There are many built-in exceptions which are raised in python when something goes
# wrong.
# Exception in python can be handled using a try statement. The code that handles the
# exception is written in the except clause.
# When the exception is handled, the code flow continues without program interruption.
# We can also specify the exception to catch like below:

# try:
#    a = int(input("Enter a number: "))
#    print(a)
# # except Exception as e:
# #    print(e)
# # except ValueError as VO:
# #    print(VO)
# # except ZeroDivisionError as v:
# #    print(v)
# except TypeError as b:
#    print(b)
# except:
#    print()

# RAISING EXCEPTIONS
# We can raise custom exceptions using the ‘raise’ keyword in python.


# TRY WITH ELSE CLAUSE and TRY WITH FINALLY
# try: 
#    a = int(input("Enter a number: "))
#    print(a)
# except Exception as e:
#    print(e)
# else:
#    raise KeyError

# try: 
#    a = int(input("Enter a number: "))
#    print(a)
# except Exception as e:
#    print(e)
# finally:
#    print("Thankyou!")

#########################################################################################################################

# from module import myFunc

# # print(myFunc)

#########################################################################################################################
# THE GLOBAL KEYWORD
# ‘global’ keyword is used to modify the variable outside of the current scope.
# a = 888
# def fun():
#    global a
#    a = 3
#    print(a)

# fun()
# print(a)

#########################################################################################################################
# ENUMERATE FUNCTION IN PYTHON
# The ‘enumerate’ function adds counter to an iterable and returns it
# l = [1,2,3,4,5]
# # index = 0
# # for item in l:
# #    print(f"The item number {index} is {item}")
# #    index += 1

# # This can be simplified by enumerate function
# for index,item in enumerate(l):
#    print(f"The item number {index} is {item}")

#########################################################################################################################
# LIST COMPREHENSIONS
# List Comprehension is an elegant way to create lists based on existing lists.
# list1 = [1,7,12,11,22,]
# list2 = [ i*i for i in list1 ]
# print(list2)