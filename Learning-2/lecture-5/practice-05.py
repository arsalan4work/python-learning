# Write a program to create a dictionary of urdu words with values as their english
# translation. Provide user with an option to look it up!
# words = {
#    "madad" : "Help",
#    "kursi" : "Chair",
#    "bura" : "Bad",
#    "shukriya" : "Thank you",
#    "jee haan" : "Yes",
#    "jee nahi" : "No",
#    "asaan" : "Easy",
# }
# word = input("Enter the word you want meaning of: ")
# print(words[word])


# 2. Write a program to input eight numbers from the user and display all the unique
# numbers (once).
# s = set()
# user1 = int(input("Enter a number: "))
# s.add(user1)
# user2 = int(input("Enter a number: "))
# s.add(user2)
# user3 = int(input("Enter a number: "))
# s.add(user3)
# user4 = int(input("Enter a number: "))
# s.add(user4)
# user5 = int(input("Enter a number: "))
# s.add(user5)
# user6 = int(input("Enter a number: "))
# s.add(user6)
# user7 = int(input("Enter a number: "))
# s.add(user7)
# user8 = int(input("Enter a number: "))
# s.add(user8)
# print(s) # Output: 1, 2, 3, 4, 5, 6, 7}

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
# my_set = {18, '18'}
# print(my_set)  # Output: {18, '18'}


# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?
# 
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(len(s)) #Output: 2


# 5. s = {}
# What is the type of 's'?
# s = {} #In python empty{} is dict for set we use set() func.
# # s = set()
# print(type(s)) #Output: <class 'dict'>


# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.
# fav_languages = {}

# fav_languages["Ali"] = input("Enter Ali's favorite language: ")
# fav_languages["Sara"] = input("Enter Sara's favorite language: ")
# fav_languages["Ahmed"] = input("Enter Ahmed's favorite language: ")
# fav_languages["Zara"] = input("Enter Zara's favorite language: ")

# print("\nFavorite Languages Dictionary:")
# print(fav_languages)



# 7. If the names of 2 friends are same; what will happen to the program in problem 6?\
# The values entered later will be updated



# 8. If languages of two friends are same; what will happen to the program in problem 6?
# Nothing will happen th values can be same


# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

# s = {8, 7, 12, "Harry", [1,2]} 
# No, I cannot have a list inside a set in Python because lists are mutable and unhashable.