# Q3: Given a string, write a function to count the frequency of each character in the string without using collections.Counter.

def char_count(s):
    freq = {}  
    for char in s:
        freq[char] = freq.get(char, 0) + 1  # Increment count
    return freq  

print(char_count("hello"))
