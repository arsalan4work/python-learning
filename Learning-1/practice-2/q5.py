# Q5: Define a class Person with attributes name, age, and a method greet() that prints a greeting message. 
# Then, create a subclass Employee that adds an employee_id attribute and overrides the greet() method to include the employee’s ID

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I am {self.name}, {self.age} years old.")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def greet(self):
        print(f"Hello, I am {self.name}, {self.age} years old, Employee ID: {self.employee_id}")

p = Person("Arsalan", 20)
p.greet()  # Output: Hello, I am Arsalan, 30 years old.

e = Employee("Raza", 26, "E112")
e.greet()  # Output: Hello, I am Raza, 25 years old, Employee ID: E123
