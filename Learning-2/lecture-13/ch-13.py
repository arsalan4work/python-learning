# VIRTUAL ENVIRIONMENT
# An environment which is same as the system interpreter but is isolated from the other
# Python environments on the system.

# INSTALLATION
# To use virtual environments, we write:
# pip install virtualenv # Install the package

# We create a new environment using:
# virtualenv myprojectenv # Creates a new venv

# The next step after creating the virtual environment is to activate it.
# We can now use this virtual environment as a separate Python installation.


#################################################################################################################
# PIP FREEZE COMMAND
# ‘pip freeze’ returns all the package installed in a given python environment along with
# the versions.

# pip freeze > requirements .txt

# The above command creates a file named ‘requirements.txt’ in the same directory
# containing the output of ‘pip freeze’.

# We can distribute this file to other users, and they can recreate the same environment
# using:
# pip install –r requirements.txt


#################################################################################################################
# LAMBDA FUNCTIONS
# Function created using an expression using ‘lambda’ keyword.
# Syntax:
# lambda arguments:expressions
# # can be used as a normal function

# def square(n):
#    return n*n
# print(square(5))

# square = lambda x:x*x
# print(square(5))
# sum = lambda a,b,c:a+b*c
# print(sum(33,12,19))


#################################################################################################################
# JOIN METHOD (STRINGS)
# Creates a string from iterable objects.
# l = ["apple", "mango", "banana", "pine apple", "orange"]
# result = ", and, ".join(l)
# print(result)
# The above line will return “apple,and,mango,and,banana”.


#################################################################################################################
# FORMAT METHOD (STRINGS)
# Formats the values inside the string into a desired output.
# template.format(p1,p2...)
# Syntax:
# a = "{} is a good {}".format("harry", "boy") #1.
# print(a)
# b = "{} is a good {0}".format("harry", "boy") #2.
# print(b)
# # output for 1:
# harry is a good boy
# output for 2:
# boy is a good harry


#################################################################################################################
# MAP, FILTER & REDUCE
# Map applies a function to all the items in an input_list.
# Syntax.
# map(function, input_list)
# # the function can be lambda function
# Filter creates a list of items for which the function returns true.
# list(filter(function))
# # the function can be lambda function
# Reduce applies a rolling computation to sequential pair of elements.
# from functools import reduce
# val=reduce (function, list1)
# # the function can be lambda function

# Map
# l = [1,2,3,4,5]
# sq = lambda x: x*x
# sqlist = map(sq, l)
# print(list(sqlist))

# Filter
# def even(n):
#    if(n%2 == 0):
#       return True
#    return False

# onlyEven = filter(even, l)

# print(list(onlyEven))

# Reduce
# from functools import reduce
# l = [1,2,3,4,5]
# def sum(a,b):
#    return a + b

# print(reduce(sum, l))