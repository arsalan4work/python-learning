# 1. Create a class “Programmer” for storing information of few programmers
# working at Microsoft.
# class Programmer:
#    company = "Microsoft"

#    def __init__(self, name, age, salary, position):
#       self.name = name
#       self.age = age
#       self.salary = salary
#       self.position = position

# david = Programmer("David", 28, 75000, "Senoir Front-end Developer")
# print(f"Company: {david.company}, Name: {david.name}, Age: {david.age}, Salary: ${david.salary}, Position: {david.position}")

# arsalan = Programmer("Arsalan", 48, 240000, "Business strategist")
# print(f"Company: {arsalan.company}, Name: {arsalan.name}, Age: {arsalan.age}, Salary: ${arsalan.salary}, Position: {arsalan.position}")

# ali = Programmer("Ali", 29, 160000, "Cloud native Developer")
# print(f"Company: {ali.company}, Name: {ali.name}, Age: {ali.age}, Salary: ${ali.salary}, Position: {ali.position}")

# andrew = Programmer("Andrew", 34, 120000, "Senoir software eng")
# print(f"Company: {andrew.company}, Name: {andrew.name}, Age: {andrew.age}, Salary: ${andrew.salary}, Position: {andrew.position}")

# jack = Programmer("Jack", 36, 80000, "Senoir back-end Developer")
# print(f"Company: {jack.company}, Name: {jack.name}, Age: {jack.age}, Salary: ${jack.salary}, Position: {jack.position}")

###############################################################################################################################
# 2. Write a class “Calculator” capable of finding square, cube and square root of a
# number.
# class Calculator:
#    def __init__(self, n):
#       self.n = n

#    def square(self):
#       print(f"The Square is {self.n * self.n}")

#    def cube(self):
#       print(f"The Cube is {self.n * self.n * self.n}")

#    def square_root(self):
#       print(f"The Square Root is {self.n ** 1/2}")

# a = Calculator(4)
# a.square()
# a.cube()
# a.square_root()


###############################################################################################################################
# 3. Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?
# class Demo():
#    a = 4

# o = Demo()
# print(o.a) #prints the class attribute because instance attribute is not present
# o.a = 0 #Instance attribute is set here
# print(o.a) #prints the instance attribute because instance is present here
# print(Demo.a)



###############################################################################################################################
# 4. Add a static method in problem 2, to greet the user with hello.
# class Calculator:

#    @staticmethod
#    def greet():
#       print("Hello There!")

#    def __init__(self, n):
#       self.n = n

#    def square(self):
#       print(f"The Square is {self.n * self.n}")

#    def cube(self):
#       print(f"The Cube is {self.n * self.n * self.n}")

#    def square_root(self):
#       print(f"The Square Root is {self.n ** 1/2}")
# a = Calculator(4)
# a.greet()
# a.square()
# a.cube()
# a.square_root()



###############################################################################################################################
# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Pakistan Railways.
# from random import randint

# class Train:

#    def __init__(self, trainNo):
#       self.trainNo = trainNo
#    def book(self, startingWith, towards):
#       print(f"Ticket is booked in train no: {self.trainNo} from {startingWith} to {towards}")

#    def getStatus(self):
#       print(f"Train no: {self.trainNo} is running on time!")

#    def getFare(self, startingWith, towards):
#       print(f"Ticket fare in train no: {self.trainNo} from {startingWith} to {towards} is {randint(3000,9999)}")

# t = Train(129)
# t.book("Karachi", "Lahore")
# t.getStatus()
# t.getFare("Karachi", "Islamabad")


###############################################################################################################################
# 6. Can you change the self-parameter inside a class to something else (say
# “arsalan”). Try changing self to “slf” or “arsalan” and see the effects.

# class Train:

#    def __init__(slf, trainNo):
#       slf.trainNo = trainNo

#    def book(arsalan, startingWith, towards):
#       print(f"Ticket is booked in train no: {arsalan.trainNo} from {startingWith} to {towards}")

#    def getStatus(self):
#       print(f"Train no: {self.trainNo} is running on time!")

#    def getFare(self, startingWith, towards):
#       print(f"Ticket fare in train no: {self.trainNo} from {startingWith} to {towards} is PKR 3200")

# t = Train(129)
# t.book("Karachi", "Lahore")
# t.getStatus()
# t.getFare("Karachi", "Islamabad")
