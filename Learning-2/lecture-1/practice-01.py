#Q1: Write a program to print Twinkle twinkle little star poem in python.

# print("""
#       Twinkle, twinkle, little star,
#       How I wonder what you are!
#       Up above the world so high,
#       Like a diamond in the sky. """)

#Q2: Use REPL and print the table of 5 using it. 
# Done!!

#Q3: Install an external module and use it to perform an operation of your interest. 

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Hello Arsalan! How are you!")
# engine.runAndWait()

# Q4: Write a python program to print the contents of a directory using the os module.
#     Search online for the function which does that. 
import os
# Specify the directory you want to list
directory_path = "/"

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print eash file and directory name
print(contents)