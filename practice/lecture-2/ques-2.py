# Write a situation where conditional statements can determine whether a person is eligible to vote based on their age. 
# If they are 18 or older, they can vote; if not, they cannot.

age = int(input("Enter your age: "))

if( age >= 18):
   print("You can vote!")
else:
   print("Sorry! you can't vote.")