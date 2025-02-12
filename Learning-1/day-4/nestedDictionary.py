# Nested Dictionary

student = {
   "name" : "Arsalan",
   "subjects" : {
      "physics" : 61,
      "maths" : 48,
      "computer" : 91,
      "english" : 84
   },
   "age" : 20
}

# Accessing Nested Dict
print(student["subjects"]["computer"])

# Dict Methods, keys(), values(), items(), get(), update()
print(student.keys()) # Print all keys
print(student.values()) # Print all values
print(student.items()) # Print all items in a tuple 
print(student ["name"]) #if i said name2 then it occurs error
print(student.get("name")) # if i said name2 then no error but -> None

print("Next/")
student.update({"city": "Karachi"}) #add key:value using update method
print(student)

# OR
new_dict = {
   "name": "Muhammad Arslan",
   "age" : 21,
}
student.update(new_dict)
print(student)