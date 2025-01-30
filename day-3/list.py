# List in Python
marks = [94.4, 88.8, 78.5, 66.3, 48.1]

print(marks)
print(marks[0])

# Immutable are strings which we can access only but not change the data
str1 = "My name is Arsalan"
print(str1[0:8])
print(str1[8:15])


# Mutable List are accessable and changeable
student1 = ["Arsalan", 20, "Karachi"]
print(student1)
# # Changing the values using index and assign
student1[0] = "Ali"
student1[1] = 23
student1[2] = "Lahore"
print(student1) #Print the changed value


# List slicing (Similar to string slicing)
num = [94, 88, 78, 66, 48]
print(num[2:3])
print(num[:3])
print(num[0:])


# List Methods append(val), sort(), sort(reverse=true), reverse(), insert(val, val)
a = [3,2,1,6,4,5,7]
print(a)
a.append(8) #Adds in last
print(a)
a.sort() #sort in acending
print(a)
a.sort(reverse=True) #Sort in decending
print(a)
a.reverse() # Reverse the value
print(a)
b = [3,2,1,6,4,5,7]
b.insert(2, 0) # similar to append but at a particular index. First val index location & second is value 
print(b)
b.remove(1) # Remove first occurence of the value
print(b)
b.pop(3) # Removes at a particular index
print(b)