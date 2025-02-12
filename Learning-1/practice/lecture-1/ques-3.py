# Write a program that takes two numbers as input and prints their sum, difference, product, and quotient. 
# Ensure to handle the division by zero case.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2

if num2 != 0:
    quot_result = num1 / num2
else:
    quot_result = "Undefined (division by zero)"

print("Sum: ",sum_result)
print("Difference: ", diff_result)
print("Product: ",prod_result)
print("Quotient: ",quot_result)
