# OOP in Python. To map with real word scenarios, we started using objects in code.

# Class is a blueprint for creating objects.
# class Student:
#    name = "Arsalan"

# s1 = Student()
# print(s1.name)

# # #
# class Car:
#    brand = "Toyota"
#    model = "Corolla 1.8 "
#    color = "black"
#    engine = "1889cc"
#    horse_power = 185

# car1 = Car()
# print(f"My car brand is {car1.brand}, model is {car1.model}, 
# color is {car1.color}, engine is {car1.engine}, horse power is {car1.horse_power}")

##############################################################################################################################
# __init__ fuction (Constructor). All classes have a function called __init__(), 
# which is always executed when the class is being initiated.

# class Student:
#    def __init__(self, fullname, marks):
#       self.name = fullname
#       self.marks = marks
#       print("Adding student data...")

# s1 = Student("Arsalan", 97)
# print(s1.name, s1.marks)

# s2 = Student("Ali", 82)
# print(s2.name, s2.marks)

##############################################################################################################################
# Methods are functions that belongs to objects.

# class Student:
#    university_name = "Welcome to UOK(University of Karachi) portal!"
#    def __init__(self, name, marks):
#       self.name = name
#       self.marks = marks

#    def get_avg(self):
#       sum = 0
#       for val in self.marks:
#          sum += val
#          print(f"Hi! {self.name}, your average marks is: {sum/3}")


# s1 = Student("Arsalan", [99, 93, 81])
# s1.get_avg()

# s1.name = "M Arsalan"
# s1.get_avg()

##############################################################################################################################
# Static methods, Methods that dont use the self parameter(work at class level)

# class Student:
#    university_name = "Welcome to UOK(University of Karachi) portal!"
#    def __init__(self, name, marks):
#       self.name = name
#       self.marks = marks

#    @staticmethod  #decorator
#    def hello():
#       print("Hello")

#    def get_avg(self):
#       sum = 0
#       for val in self.marks:
#          sum += val
#          print(f"Hi! {self.name}, your average marks is: {sum/3}")


# s1 = Student("Arsalan", [99, 93, 81])
# s1.get_avg()

# s1.name = "M Arsalan"
# s1.get_avg()


