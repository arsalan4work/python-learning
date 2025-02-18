# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
# present, a message without exiting the program must be printed prompting the same.
# try: 
#    with (
#    open("file1.txt", "r") as f1,
#    open("file2.txt", "r") as f2,
#    open("file3.txt", "r") as f3,
#    ):
#       print(f"File 1 has: {f1.read()}, File 2 has: {f2.read()}, File 3 has: {f3.read()}")
# except Exception as e:
#    print(e)


#########################################################################################################################
# 2. Write a program to print third, fifth and seventh element from a list using enumerate
# function.
# list1 = [1,2,3,4,5,6,7,8,9,0]
# for i, item in enumerate(list1):
#    if i == 2 or i == 4 or i == 6:
#       print(item)

#########################################################################################################################
# 3. Write a list comprehension to print a list which contains the multiplication table of a
# user entered number.
# n = int(input("Enter a number: "))
# table = [n*i for i in range(1,11)]
# print(table)


#########################################################################################################################
# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionError’.
# try:
#    a = int(input("Enter a: "))
#    b = int(input("Enter b: "))
#    print(a/b)
# except ZeroDivisionError as z:
#    print(f"Infinite: {z}")


#########################################################################################################################
# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.
# n = int(input("Enter a number: "))
# table = [n*i for i in range(1,11)]
# print(table)

# with open("tables.txt", "a") as f:
#    f.write(f" Table of {n}: {str(table)}\n")