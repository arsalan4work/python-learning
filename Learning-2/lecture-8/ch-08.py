# A function is a group of statements performing a specific task.
# When a program gets bigger in size and its complexity grows, it gets difficult for a
# program to keep track on which piece of code is doing what!

# def avg():
#    a = int(input("Enter a number: "))
#    b = int(input("Enter a number: "))
#    c = int(input("Enter a number: "))

#    average = (a+b+c) /3
#    print(average)

# avg()
# avg()
# avg()
# avg()
# avg()

# Quick Quiz: Write a program to greet a user with “Good day” using functions
# def func(name, ending): # A function can accept some value it can work with. We can put these values in the parentheses.
#    print(f"Good day {name}")
#    print(ending)
#    return "Done!"

# func("Arsalan", "Thankyou!") 
# func("Ali ", "Thankyou!") 
# func("Zoya", "Thanks!") 

# a = func("Arsalan", "Thanks!!")
# print(a)

# We can have a value as default as default argument in a function.
# If we specify name = “stranger” in the line containing def, this value is used when no
# argument is passed.

# def goodDay(name, ending="Thankyou"):
#    print(f"Good Day, {name}")
#    print(ending)
# goodDay("Arsalan")

########################################################################################################################33
# Recursion is a function which calls itself.
# It is used to directly use a mathematical formula as function.

def factorial(n):
   if (n == 1 or n == 0):
      return 1
   return n * factorial(n-1)

n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")