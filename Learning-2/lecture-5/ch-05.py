# Dictoionaries are mutable, indexed, unordered, cannot contain duplicate keys
# marks = {
#    "Arsalan": 98,
#    "Ali": 88,
#    "Ahmed": 89,
# }

# print(marks)
# print(marks["Arsalan"])

# Dictionary Methods
# print(marks.items()) #Return in tuple
# print(marks.keys()) # Return all keys
# marks.update({"Arsalan" : 97}) # Updates the dictionary with supplied key-value pairs.
# print(marks)
# print(marks.get("Arsalan")) # Returns the value of the specified key. or NONE!

####################################################################################################################################################
# Sets is a collection of non-repetitive elements.
# PROPERTIES OF SETS
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.

# s = {1,2,3}
# print(s)
# e = set() #Dont use e = {} as it will create an empty dictionary

# Sets methods
# s.add(4) #add
# print(s)

# # Clear() all elements from the sets
# s.clear()
# print(s)

# Copy() runs a shallow copy of set
# a = s.copy()
# print(a)

# Difference() and diffrence_update()
# s1 = {1,2,3}
# s2 = {3,4,5}

# print(s1.difference(s2))
# print(s1.difference_update(s2))
# print(s1)

# pop() removes random value
# s = {1,2,3,4,5}
# s.pop()
# print(s)

# Union() and intersection()
s1 = {1,2,3,4,5}
s2 = {5,4,6,7}
print(s1.union(s2)) # print unqiue values
print(s1.intersection(s2)) #print common values