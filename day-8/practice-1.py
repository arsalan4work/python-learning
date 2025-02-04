# # Create a studdent class that takes names & marks of 3 subjects as aurguments in constructor.
# # then create a method to print that average.

class Student:
   university_name = "Welcome to UOK(University of Karachi) portal!"
   def __init__(self, name, marks):
      self.name = name
      self.marks = marks

   def get_avg(self):
      sum = 0
      for val in self.marks:
         sum += val
         print(f"Hi! {self.name}, your average marks is: {sum/3}")


s1 = Student("Arsalan", [99, 93, 81])
s1.get_avg()

s1.name = "M Arsalan"
s1.get_avg()
