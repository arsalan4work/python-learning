# 1. Write a program to find the greatest of four numbers entered by the user.
# a1 = int(input("Enter a number: "))
# a2 = int(input("Enter a number: "))
# a3 = int(input("Enter a number: "))
# a4 = int(input("Enter a number: "))

# if (a1>a2 and a1>a3 and a1>a4):
#    print(f"1st number is greater:  {a1}")
# elif (a2>a1 and a2>a3 and a2>a4):
#    print(f"2nd number is greater:  {a2}")
# elif (a3>a1 and a3>a2 and a3>a4):
#    print(f"3rd number is greater:  {a3}")
# else:
#    print(f"Greater number is {a4}")

# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.
# phy = int(input("Enter physics marks: "))
# math = int(input("Enter maths marks: "))
# sci = int(input("Enter science marks: "))

# total_percentage = (100 *(phy + math + sci) / 300)
# if(total_percentage >= 40 and phy>=33 and math>=33 and sci>=33):
#    print("You are passed!")
# else:
#    print("You failed!")



# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.
# p1 = "Make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "click this"

# message = input("Enter your comment: ")
# if (p1 in message or p2 in message or p3 in message or p4 in message):
#    print("You are spaming")
# else:
#    print(message)


# 4. Write a program to find whether a given username contains less than 10
# characters or not.
# username = input("Enter your name: ")
# if (len(username) <= 10):
#    print(username)
# else:
#    print("User name is more than 10 characters")


# 5. Write a program which finds out whether a given name is present in a list or not.
# l1 = ["Arsalan", "Ali", "Ahmed", "Salar"]
# name = input("Enter your name: ")
# if name in l1:
#    print("Name found!")
# else: 
#    print("Name not found!")


# 6. Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F
# marks = int(input("Enter your marks: "))
# grade = ["A+", "A", "B", "C", "D", "F"]

# if (marks <= 100 and marks >= 90):
#    print(f"Your grade is {grade[0]}")
# elif (marks <= 90 and marks >= 80):
#    print(f"Your grade is {grade[1]}")
# elif (marks <= 80 and marks >= 70):
#    print(f"Your grade is {grade[2]}")
# elif (marks <= 70 and marks >= 60):
#    print(f"Your grade is {grade[3]}")
# elif (marks <= 60 and marks >= 50):
#    print(f"Your grade is {grade[4]}")
# else:
#    print(f"You failed: {grade[5]}")



# 7. Write a program to find out whether a given post is talking about “Arsalan” or not.

post = "Arsalan is learning Python and AI."

if "arsalan" in post.lower():
    print("The post is talking about Arsalan.")
else:
    print("The post is NOT talking about Arsalan.")
