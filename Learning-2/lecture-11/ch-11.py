# Inheritance is a way of creating a new class from an existing class.

# class Employee:
#    company = "ITC"
#    def show(self):
#       print(f"The name of the employee is {self.name} and the salary is {self.salary}")

# class Programmer(Employee):
#    company = "ITC Infotech"
#    def showLanguage(self):
#       print(f"The name is {self.name} and he is good with {self.language} language")

# a = Employee()
# b = Programmer()
# print(a.company, b.company)

##########################################################################################################################
# Multiple Inheritance

# class Employee:
#    company = "ITC"
#    name = "Arsalan"
#    def show(self):
#       print(f"The name of the employee is {self.name} and the company is {self.company}")

# class Coder:
#    language = "Python"
#    def printLanguages(self):
#       print(f"Out of all the languages here is your language {self.language}")

# class Programmer(Employee, Coder):
#    company = "ITC Infotech"
#    def showLanguage(self):
#       print(f"The name is {self.company} and he is good with {self.language} language")

# a = Employee()
# b = Programmer()
# b.show()
# b.printLanguages()
# b.showLanguage()

##########################################################################################################################
# MultiLevel Inheritance

# class Employee:
#    a = 1
   

# class Programmer(Employee):
#    b = 2

# class Manager(Programmer):
#    c = 3

# o = Employee()
# print(o.a) #Prints the a attribute
# # print(o.b) ## shows an error as there is no b attribute in Employee class

# o = Programmer()
# print(o.a, o.b) #no error but when we write o.c it make error

# o = Manager()
# print(o.a, o.b, o.c) #no error 

##########################################################################################################################3
# Super() method is used to access the methods of a super class in the derived class.

# class Employee:
#    def __init__(self):
#       print("Constructor of Employee")
#    a = 1
   

# class Programmer(Employee):
#    def __init__(self):
#       super().__init__()
#       print("Constructor of Programmer")
#    b = 2

# class Manager(Programmer):
#    def __init__(self):
#       super().__init__()
#       print("Constructor of Manager")
#    c = 3

# # o = Employee()
# # print(o.a)

# # o = Programmer()
# # print(o.a, o.b) 

# o = Manager()
# print(o.a, o.b, o.c)



# ########################################################################################################################## 

# A @classmethod is a method which is bound to the class and not the object of the class.

# class Employee:
#    a = 1
#    @classmethod #decorator
#    def show(cls):
#       print(f"The class attribute of a is {cls.a}")

# e = Employee()
# e.a = 45
# e.show()

##########################################################################################################################
# @PROPERTY DECORATORS
# class Employee:
#    a = 1
#    @classmethod #decorator
#    def show(cls):
#       print(f"The class attribute of a is {cls.a}")

#    @property #decorator
#    def name(self):
#       return f"{self.fname} {self.lname}"
   
#    @name.setter #decorator
#    def name(self, value):
#       self.fname = value.split(" ") [0]
#       self.lname = value.split(" ") [1]

# e = Employee()
# e.a = 45
# e.show()

# e.name = "Arsalan Arsss"
# print(e.fname, e.lname)
# e.show()

# If e = Employee() is an object of class employee, we can print (e.name) to print the
# ename by internally calling name() function.

##########################################################################################################################
# Operators in Python can be overloaded using dunder methods.
# These methods are called when a given operator is used on the objects.
# class Number:
#    def __init__(self, n):
#       self.n = n

#    def __add__(self, num):
#       return self.n + num.n
   
# n = Number(1)
# m = Number(2)
# print(n+m)

# p1+p2 # p1.__add__(p2)
# p1-p2 # p1.__sub__(p2)
# p1*p2 # p1.__mul__(p2)
# p1/p2 # p1.__truediv__(p2)
# p1//p2 # p1.__floordiv__(p2)

# Other dunder/magic methods in Python:
# str__() # used to set what gets displayed upon calling str(obj)
# 45
# __len__() # used to set what gets displayed upon calling.__len__() or
# len(obj)
