# Store following word meaning in a python dictionary:
# table: "A piece of furniture", "list of facts & figures"
# cat: "A small animal"

# dictionary = {
#    "car": "A small animal",
#    "table" : ["A piece of furniture", "List of facts & figures"]
# }

# print(dictionary)


#  you are given a list of subjects for students. Assume one classrom is 
# required for 1 subject. How many classrooms are needed by all students
# "python", "java", "C++", "python", "javascript", "java", 
# "python", "java", "C++", "C"

# classrooms = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
# print(classrooms)
# print(len(classrooms))


# Write a program to enter marks of 3 subjects from the user and store
# them in a dictionary. Start with an empty dictionary & add one by one. 
# Use subjects name as keys & marks as value.
# marks = {}
# x = int(input("Enter your physics marks: "))
# marks.update({"phy" : x})
# x = int(input("Enter your maths marks: "))
# marks.update({"maths" : x})
# x = int(input("Enter your chemistry marks: "))
# marks.update({"chemistry" : x})
# print(marks)


# Figure out a way to store 9 & 9.0 as seperate values in the set. 
# (Your can take help of built in data types)
values = {
   ("float", 9.0),
   ("int", 9),
}
print(values)