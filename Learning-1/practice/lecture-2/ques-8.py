# Given a list of integers, write a function to find the maximum number in the list without using the built-in max() function.

numbers = [10, 21, 32, 43, 8]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print("The maximum number is:", max_num)
