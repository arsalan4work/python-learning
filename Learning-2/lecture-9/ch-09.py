# FILE I/O

### File read "r"
# f = open("file.txt", "r")
# data = f.read()
# print(data)
# f.close()

### File write "w"
# st = "Hi, My name is Arsalan. I am 20 years old."

# f = open("myfile.txt", "w")
# f.write(st)
# f.close()


### We can also use f.readline() function to read one full line at a time
# f = open("file.txt")
# # lines = f.readlines()
# # print(lines)
# # lines = f.readline()
# # print(lines)
# # f.close()
# line = f.readline()
# while (line != ""):
#    print(line)
#    line = f.readline()
# f.close()


### "a" for append in file in last 
# st = "Arsalan!, Arsalan"
# f = open("file.txt", "a")
# f.write(st)
# f.close

### The best way to open and close the file automatically is the "with" statement.
# Open the file in read mode using 'with', which automatically closes the file
with open("myfile.txt", "r") as f:
   text = f.read()
print(text)