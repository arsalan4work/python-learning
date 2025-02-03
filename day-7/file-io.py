# File I/O. 'r' Read(default), 'w' open for writing(first delete the data then overwrite), 
# 'x' open for writing appending to the end of the file if it exist, 'b' binary mode,
# 't' text mode, '+' open a disk file for updating(r and w).
##########################################################################################################################
# For Read (Only read the data)
# f = open("demo.txt", "r")
# data = f.readline()
# print(data)
# print(type(data))

##########################################################################################################################
# For write (or if file doesn't exist write mode create for me)
# f = open("demo.txt", "w")
# f.write("I want to learn nextjs by tomorrow. Now i want to learn python")
# f.close()

##########################################################################################################################
# For Append (Add in the last)
# f = open("demo.txt", "a")
# f.write("\nI have to learn python\n")
# f.close()

##########################################################################################################################
# Read and Write r+ (For overwrite from the start)
# f = open("demo.txt", "r+")
# f.write("\nI have to do a python task\n")
# print(f.read())
# f.close()

##########################################################################################################################
# Read and Write w+ (tuncate all the data and start new)
# f = open("demo.txt", "w+")
# print(f.read())
# f.write("I have to do a python task\n")
# f.close()

##########################################################################################################################
# Read and Write a+ (read and write to append)
# f = open("demo.txt", "a+")
# print(f.read())
# f.write("I have to do a python task\n")
# f.close()

##########################################################################################################################
# with open syntax (Auto close file, )
# with open("demo.txt", "r") as f:
#    data = f.read()
#    print(data)


##########################################################################################################################
# # Deleting a file (module (like a code library) is a file written by another programer that generally has a func we can use)
# # using the os module like..

# import os
# os.remove("demo.txt")

with open("practice.txt", "r") as f:
   data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
   f.write(new_data)