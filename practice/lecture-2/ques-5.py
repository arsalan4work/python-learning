# Discuss how you would identify whether a list of numbers [10, 21, 32, 43] 
# contains even or odd numbers. What method would you use to categorize them?

numbers = [10, 21, 32, 43]

for num in numbers:
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")


