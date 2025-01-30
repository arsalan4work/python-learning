# Create a program that prompts the user to enter a number as a string and then converts it to an integer.
#  Print the converted value and its type.

userInput = input("Enter a number: ")
userInput_Int = int(userInput)
print("You have entered: ", userInput_Int)
print(type(userInput_Int))