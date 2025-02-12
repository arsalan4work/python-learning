# Q2: Write a Python function that takes a list of integers and 
# returns a new list with the squares of each number, sorted in descending order.


def list_of_int(num):
   return sorted([nums ** 2 for nums in num], reverse=True)

print(list_of_int([1,3,4,2,5]))