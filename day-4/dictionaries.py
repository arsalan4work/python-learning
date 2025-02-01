# Dictionaries are used to store data value in key:value pairs 

# Dictionaries are mutable, unordered, and don't allow to duplicate keys.
info = {
   "name" : "Arsalan",
   "subject" : ["Nextjs", "Python", "TypeScript"],
   "topics" : ("dict", "set"),
   "age" : 20,
   "is_adult" : True,
   "marks" : 93.32,
}

info["name"] = "Muhammad Arsalan" #change value
info["lastname"] = "Suleman" #add value
info["age"] = 21 #change value
print(info)
print(info["name"]) #access specific value
print(info["topics"])

# Or we can create null dictionary and assign value after creating
null_dict = {}
null_dict["name"] = "Arsalan"
null_dict["age"] = 20
null_dict["isadult"] = True
print(type(null_dict))
print(null_dict)