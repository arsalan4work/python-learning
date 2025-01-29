# Airthematic Operator
a = 5
b = 5
sum = a + b
print(sum)
# Or Directly Print
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #Remainder
print(a**b) #a^b 


# Relational/Comparison Operator
print("Next/")
a = 30
b = 50

print("A is equals to B: ",a == b) #False
print("A is not equals to B: ",a != b) #True
print("A is greater than B: ",a > b) #False
print("A is less than B: ",a < b) #True
print("A is greater than equals to B: ",a >= b) #False
print("A is less than equals to B: ",a <= b) #True


# Assignment Operators
print("Next/")
num = 10
num = num + 15 #This is also Correct
num += 20 # Plus and Equals
num -= 30 # Minus and Equals
num *= 40 # Multiply and Equals
num /= 50 # Divide and Equals
num %= 60 # Remainder and Equals

print(num)

# Power Operator
num1 = 2
num1 **= 5
print(num1)


# Logical Operators
print("Next/")
# Not Operator
a1 = 50
b1 = 30
print(not (a1 > b1)) #False
print(not (a1 < b1)) #True

# And Operator
val1 = True
val2 = False
# val2 = True
print("And Operator: ", val1 and val2) #If both Values are same print True else False.
print("OR Operator: ", val1 or val2) #If any Value are True print Ture else False.
print("OR Operator: ", (a1 == b1) or (a1 > b1)) 