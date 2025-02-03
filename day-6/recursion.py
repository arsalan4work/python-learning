# When a func calls it self repeatedly is recursion. Recursion and loops usecases are same in majority cases.

# def show(n):
#    if(n == 0):
#       return
#    print(n)
#    show(n-1)

# user_input = int(input("Enter a number to reverse it to 1: "))
# show(user_input)


def fact(n):
   if(n == 1 or n == 0):
      return 1
   return fact(n-1) * n

print(fact(5))