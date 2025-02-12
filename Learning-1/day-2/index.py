#Accessing in this string with index number
string = "My name is Arsalan"
print(string[3])


# Slicing Method
str1 = "My name is Arsalan"
print(str1[0:8])
print(str1[8:15])
print(str1[14:18])
print(str1[3:len(str1)])
print(str1[14:]) #[14: to end]
print(str1[:18]) #[0: 18]

# Negative Slicing
str2 = "Arsalan"
print(str2[-7: -1])
