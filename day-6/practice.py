# # Write a program to print the length of a list.

# cities = ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta", "Sialkot", "Faisalabad"]
# heros = ["Thor", "Ironman", "Spiderman", "Batman", "Captain america"]

# def find_len(list):
#    print(len(list))

# find_len(cities)
# find_len(heros)

# # Write a program to print the element of a list in a single line.
# def print_list(list1):
#    for item in list1:
#       print(item, end=" ")

# print_list(heros)

# print("Next/")
# # Write a function to find factorial of n.(n is the parameter).
# n = 5
# def cal_fact(n):
#    fact = 1
#    for i in range(1,n+1):
#       fact *= i
#    print(fact)

# cal_fact(5)


# # Write a function to convert USD to PKR.
# def converter(usd_val):
#    pkr_val = usd_val * 278
#    print(usd_val, "USD= ", pkr_val, "PKR")

# usd_input = int(input("Enter the amount in USD: "))

# converter(usd_input)


# Write a recursive function to calculate the sum of first n natural numbers.

# def cal_sum(n):
#    if(n == 0):
#       return 0
#    return cal_sum(n-1) + n
   
# user_input = int(input("Enter a natual number: "))
# cal_sum(user_input)
# print(user_input)


#Write a recursive function to print all elements in a list. Hint: use list & index as parameter

def print_list(list, idx=0):
   if(idx == len(list)):
      return
   print(list[idx])
   print_list(list, idx+1)

names = ["Arsalan", "Ali", "Abbas", "Fahad", "Ashir"]
print_list(names)