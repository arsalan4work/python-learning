# Del func
# class Student:
#    def __init__(self, name):
#       self.name = name

# s1 = Student("Arsalan")
# print(s1.name)
# del s1
# print(s1)

# private attributes & methods are meant to be used only within the class and are not accessible from outside the class
# class Account:
#    def __init__(self, acc_no, acc_pass):
#       self.__acc_no = acc_no  #2 __ for privatize
#       self.__acc_pass = acc_pass

#    def reset_pass(self):
#       print(self .__acc_pass)

# acc1 = Account("12345", "abcde")

# print(acc1.acc_no)
# print(acc1.acc_pass) 

# class Person:
#    __name = "Anonymous"

#    def __hello(self):
#       print("Hello person")

#    def welcome(self):
#       self.__hello(self.__name)


# p1 = Person()
# print(p1.welcome())


##################################################################################################################################3
# # Inheritance, when one class(child/derived) derives the properties & methods of another class(parent/base).
# inheritance types 1. Single inheritance, 2. Mukti-level inheritance, 3. Multiple inheritance

# Single Inheritance
# class Car:
#    color = "black"
#    @staticmethod
#    def start():
#       print("Car started..")

#    @staticmethod
#    def stop():
#       print("Car stopped!")

# class ToyotaCar(Car):
#    def __init__(self, name):
#       self.name = name 

# car1 = ToyotaCar("Corolla")
# car2 = ToyotaCar("Fortuner")

# print(car1.color)


# Multi-Level inheritance

# class Car:
#    color = "black"
#    @staticmethod
#    def start():
#       print("Car started..")

#    @staticmethod
#    def stop():
#       print("Car stopped!")

# class ToyotaCar(Car):
#    def __init__(self, brand):
#       self.brand = brand

# class Fortuner(ToyotaCar):
#    def __init__(self, types):
#       self.types = types

# car1 = Fortuner("diesel")
# print(car1.start()) 


# Multiple inheritance
# class A:
#    varA = "Welcome to class A"

# class B:
#    varB = "Welcome to class B"

# class C(A,B):
#    varC = "Welcome to class C"

# c1 = C()
# print(c1.varC)
# print(c1.varA)
# print(c1.varB)


# Super() method is used to access methods of the parent class.

# class Car:
#    def __init__(self, types):
#       self.types = types

#    @staticmethod
#    def start():
#       print("Car started..")

#    @staticmethod
#    def stop():
#       print("Car stopped!")

# class ToyotaCar(Car):
#    def __init__(self, name, types):
#       super().__init__(types)
#       self.name = name
#       super().start()

# car1 = ToyotaCar("Prius", "Electric")
# print(car1.types)


# @classmethod, class method is bound to the class & recieves the class as an implicit first argument.
# Note: static method can't access or modify class state &  generally for utility.

# class Person:
#    name = "anonymous"

#    # def changeName(self, name):
#    #    self.name = name   # #indirect methods: self.__class__. OR Person.name
#    @classmethod # # decorator
#    def changeName(cls, name):
#       cls.name = name

# p1 = Person()
# p1.changeName("Arsalan")
# print(p1.name)


# # we use @property decorator on any method in the class to use the method as property.

class Student:
   def __init__(self, phy, chem, math):
      self.phy = phy
      self.chem = chem
      self.math = math
   #    self.percentage = str((self.phy + self.chem + self.math) / 3 + "%")

   # def calcPertcentage(self):
   #    self.percentage = str((self.phy + self.chem + self.math) / 3 + "%")
   @property # # decorator
   def percentage(self):
      return str((self.phy + self.chem + self.math) / 3) + "%"

st1 = Student(98, 97, 99)
print(st1.percentage)

st1.phy = 86
print(st1.percentage)