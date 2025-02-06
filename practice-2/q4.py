# Q4: Write a Python function that checks whether a given string 
# is a palindrome (reads the same forwards and backwards) while ignoring spaces and punctuation.


import re  

def is_palindrome(s):
    clean_s = re.sub(r'["^a-zA-Z0-9"]', '', s).lower()  # Remove non-alphanumeric characters
    return clean_s == clean_s[::-1]  # Compare with reverse

print(is_palindrome("Madam, in Eden, I'm Adam."))  # Output: False
