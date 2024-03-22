# Convert one form of collections to the other

# STRINGS

# String to List
str1 = "RUSHABH"
list1 = list(str1)
print(list1)

# String to Tuple
str1 = "RUSHABH"
tuple1 = tuple(str1)
print(tuple1)

# String to Set
str1 = "RUSHABH"
set1 = set(str1)
print(set1)

# String to Dictionary
str1 = "RUSHABH"
dict1 = {i+1: j for i, j in enumerate(str1)}
dict2 = {j: i+1 for i, j in enumerate(str1)}  # will update repeated letter with last position
print(dict1)
print(dict2)
print()


# LISTS

# List to string
list1 = [1, 2, 3, 4]
str1 = str(list1)  # Will print like [1, 2, 3, 4] with brackets
str2 = ""
for i in list1:  # Will properly print all list values stuck together like in a string
    str2 = str2 + str(i)
print(str1)
print(str2)

# List to tuple
list1 = [1, 2, 3, 4]
tuple1 = tuple(list1)
print(tuple1)

# List to Set
list1 = [1, 2, 3, 4]
set1 = set(list1)
print(set1)

# List to Dictionary
list1 = ["a", "b", "c", "d"]
dict1 = {j: i+1 for i, j in enumerate(list1)}
dict2 = {i+1: j for i, j in enumerate(list1)}
print(dict1)
print(dict2)
print()


# TUPLES

# Tuple to String
tuple1 = (1, 2, 3, 4)
str1 = str(tuple1)  # Will print (1, 2, 3, 4) with brackets
print(str1)
str2 = ""
for i in tuple1:  # Will print properly like a string
    str2 = str2 + str(i)
print(str2)

# Tuple to List
tuple1 = (1, 2, 3, 4)
list1 = list(tuple1)
print(list1)

# Tuple to Set
tuple1 = (1, 2, 3, 4)
set1 = set(tuple1)
print(set1)

# Tuple to Dictionary
tuple1 = ('a', 'b', 'c', 'd')
dict1 = {i+1: j for i, j in enumerate(tuple1)}
dict2 = {j: i+1 for i, j in enumerate(tuple1)}
print(dict1)
print(dict2)
print()


# SETS

# Set to String
set1 = {1, 2, 3, 4, 5}
str1 = str(set1)
print(str1)

set2 = {'a', 'b', 'd', 'c'}
str2 = str(set2)
print(str2)
