# Solving a problem by creating object is one of the most popular approaches in
# programming. This is called object-oriented programming.
# This concept focuses on using reusable code (DRY Principle).
# CLASS
# A class is a blueprint for creating object.

# class Employee:
#    language = "Python" #This is a class attribute
#    salary = 10000

#    def getInfo(self):
#       print(f"The Language is: {self.language}. The Salary is: {self.salary}.")

# arsalan = Employee()
# arsalan.name = "Arsalan" #This is a instance attribute
# print(arsalan.name, arsalan.language, arsalan.salary)

# ali = Employee()
# ali.name = "Ali"
# ali.salary = "15000"
# print(ali.name, ali.language, ali.salary)
# ^ Here name is instance attribute and salary and language are class attribute as they directly belong to the class

# arsalan.getInfo()
# Employee.getInfo(arsalan)

# class Employee:
#    language = "Python" #This is a class attribute
#    salary = 10000

#    def getInfo(self):
#       print(f"The Language is: {self.language}. The Salary is: {self.salary}.")

#    @staticmethod
#    def greet():
#       print(f"Good Morning!")

# arsalan = Employee()
# arsalan.greet()
# arsalan.getInfo()

###############################################################################################################################
# __INIT__() CONSTRUCTOR
# __init__() is a special method which is first run as soon as the object is created.
# __init__() method is also known as constructor.
# It takes ‘self’ argument and can also take further arguments.

# class Employee:
#    language = "Python" #This is a class attribute
#    salary = 10000

#    def __init__(self): #Dunder method which is automatically called
#       print("I am create an object")

#    def getInfo(self):
#       print(f"The Language is: {self.language}. The Salary is: {self.salary}.")

#    @staticmethod
#    def greet():
#       print(f"Good Morning!")

# arsalan = Employee()
# arsalan.greet()
# arsalan.getInfo()
