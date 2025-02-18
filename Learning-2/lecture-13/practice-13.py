# 1. Create two virtual environments, install few packages in the first one. 
# How do you create a similar environment in the second one?
# Done!

#############################################################################################################
# 2. Write a program to input name, marks, and phone number of a student 
# and format it using the format function like below:
# "The name of the student is Arsalan, his marks are 88 and phone number is 99999888"
# name = input("Enter your name: ")
# marks = int(input("Enter your marks: "))
# phone = int(input("Enter your Phone number: "))

# s = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone)
# print(s)


#############################################################################################################
# 3. A list contains the mumtiplication table of 7. Write a program to convert it to vertical string of the numbers
# table = [str(7*i) for i in range(1,11)]

# s = "\n".join(table)
# print(s)


#############################################################################################################
# 4. Write a program to filter a list of numbers which are divisible by 5
# def devisible(n):
#    if(n%5 == 0):
#       return True
#    return False

# a = [1,2,3,4,5,6,7,8,9,0]
# f = list(filter(devisible, a))
# print(f)


#############################################################################################################
# 5. Write a program to find the maximum of the numbers in a list using the reduce function
# from functools import reduce
# a = [1,2,3,4,5,6,7,8,9,0]
# def greater(a,b):
#    if (a>b):
#       return a
#    return b

# print(reduce(greater, a))


#############################################################################################################
# 6. Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.
# Done!

#############################################################################################################
# 7. Explore the "Flask" module and create a web server using Flask & Python