# Set is the collection of the unordered items.
# Each element in the set must be unique & immutable
#Acceptable values in set is bool, int, float, str, tuple,
#Non- Acceptable values in set is list and dict because they are mutable.
# Sets are mutable but, set --> elements are immutable

collection = {1,2,2,4,5, "Hello", "World", "World"} # --> Sets, unordered
print(collection) # --> unordered
print(type(collection))
print(len(collection)) # --> total number of items


# Set Methods add(), remove(), clear(), pop() union(), intersection()
collection2 = set()
collection2.add(1) #add value
collection2.add(2) #add (value)
collection2.add("World Hello!") #Strings
collection2.add((1,2,3,4,5)) #Tuple
print(collection2)
collection2.remove(1) #remove value
print(collection2)
collection2.pop() #Generate pop() random value
print(collection2)
collection2.clear() #Emties all values
print(collection2)

# 
set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2)) #{1,2,3,4,5} # combines both set value & return new

print(set1.intersection(set2)) #{3} #combines comman values and return new
