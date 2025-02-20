# Coding Problems (50 Marks)
# (10 Marks each)
# Write a Python function that takes a list of numbers and returns the maximum and minimum values from the list.
# def list_of_num(numbers):
#     if not numbers:
#         return None
    
#     max_value = max(numbers)
#     min_value = min(numbers)
    
#     return max_value, min_value

# num_list = [1,99,108,256,512,1024,3,5,6,901]
# max_num, min_num = list_of_num(num_list)

# print(f"Maximum: {max_num}, Minimum: {min_num}")



#######################################################################################################################################################3
# Write a Python program to check if a given string is a palindrome (reads the same forwards and backwards).
# def is_palindrome(s):
#    s = s.lower().replace(" ", " ") #Removes empty spaces
#    return s == s[::-1]

# val = input("Enter a word: ")
# if is_palindrome(val):
#    print("This is a palindrome")
# else:
#    print("Not a Palindrome")


#######################################################################################################################################################
# Create a class called Rectangle that has attributes for width and height. Include methods to calculate the area and perimeter of the rectangle.
# class Rectangle:
#    def __init__(self, width, height):
#       self.width = width
#       self.height = height

#    def area(self):
#       return self.width * self.height
   
#    def perimeter(self):
#       return 2 * (self.width + self.height)
   
# rect = Rectangle(2,5)
# print(f"Width: {rect.width}")
# print(f"Height: {rect.height}")
# print(f"Area: {rect.area()}")
# print(f"Perimeter: {rect.perimeter()}")


#######################################################################################################################################################
# Write a Python function that takes a string and returns a dictionary with the count of each character in the string.
# def char_count(s):
#    count_dict = {}

#    for char in s:
#       count_dict[char] = count_dict.get(char, 0) + 1

#    return count_dict

# string = "Hello Arsalan"
# result = char_count(string)
# print(result)


#######################################################################################################################################################
# Implement a simple program that reads a text file and counts the number of words in it. Handle any exceptions that may occur during file operations.
# def count_word_in_file(filename):
#    try:
#       with open(filename, "r") as f:
#          text = f.read()
#          words = text.split()
#          return len(words)
#    except FileNotFoundError:
#       print(f"Error: The file {filename} was not found!")
#       return None
   
# file_name = "sample.txt"
# word_count = count_word_in_file(file_name)
