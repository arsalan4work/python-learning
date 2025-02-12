# Input from user
# name = input("Enter your name: ")
# print("Welcome", name) #By Default String Data Type

# Use type casting instead in input
# age = int(input("Enter Number: "))
# print("Your age is",age)

# 
# floatingNumber = float(input("Enter Number in Decimal: "))
# print("The value is",floatingNumber)

# Proper function
name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your percentage in matric: "))

print("Your name is",name, ", your age is",age,"and your matric percentage is", marks,"%" )

confirm = input("Type confirm to double check your info: ")
print("You have confirmed that your name is",name, ", your age is",age,"and your matric percentage is", marks,"%" )
