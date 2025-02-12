# Write a program that takes two integer inputs and prints "True" if the first number 
# is greater than or equal to the second number; otherwise, print "False".

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if((num1 > num2) or (num1 == num2)):
   print(True)
else:
   print(False)