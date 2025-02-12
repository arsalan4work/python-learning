# Create a function that checks if a given string is a palindrome 
# (reads the same forwards and backwards). For example, the input "racecar" should return True

word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
