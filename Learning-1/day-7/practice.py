# Create a new file "practice.txt" using python. Add the following data in it.
# Hi everyone
# We are learning file I/O
# using Java.
# I like programming in Python

# with open("practice.txt", "w+") as f:
#    f.write("Hi everyone\nWe are learning file I/O\nusing Java\nI like programming in Python")
#    print(f.read())


#######################################################################################################################3
# Write a program that replaces all occurences of "Java" with "Python" in above file.
# with open("practice.txt", "") as f:
#    f.write

#######################################################################################################################3
# Write a program to search word "learning" exist in the file or not.
# with open("practice.txt", "r") as f:
#    data = f.read()
#    word = "learning"
#    if(data.find(word) != -1):
#       print("Found!")
#    else:
#       print("Not Found")


#######################################################################################################################3
# Write a program to find in which line of code does the word "learning" occur first
# Print -1 if word not found.
# def check_fot_line():
#    word = input("Enter a word to find: ")
#    data = True
#    line_no = 1
#    with open("practice.txt", "r") as f:
#       while data: 
#          data = f.readline()
#          if(word in data):
#             print(line_no)
#             return
#          line_no += 1

#    return -1
# check_fot_line()


#######################################################################################################################3
# From a file containing numbers seperated by comma, print the count of even numbers.

count = 0
with open("number.txt", 'r') as f:
   data = f.read()
   print(data)

   nums = data.split(",")
   for val in nums:
      if(int(val) %2 == 0):
         count += 1

print(count)
