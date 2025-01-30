# Write a program to ask user to enter name of their 3 favorites movies & store them in a list
# movies = []

# mov = input("Enter 1st movies: ")
# movies.append(mov)
# mov = input("Enter 2nd movies: ")
# movies.append(mov)
# mov = input("Enter 3rd movies: ")
# movies.append(mov)

# print(movies)


# Write a program to check if a list contains a palindrome of elements. (Hint: use copy() method).

# list1 = [1,2,1]
# list2 = [1,2,3]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#    print("This is a palindrome!")
# else:
#    print("Not palindrome!")

# Write a program to count the number of students with "A" grade in the following tuple.
# ["C", "D", "A", "A", "B", "B", "A"]

grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

# Now store the above values in a list % sort them from "A" to "B".
grade1 = ["C", "D", "A", "A", "B", "B", "A"]
grade1.sort()
print(grade1)