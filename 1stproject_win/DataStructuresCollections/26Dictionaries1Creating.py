# Collection problems
# Dictionaries 1
# Creating Dictionaries (even with lists)

# Method 1 : comma-separated key:value pairs in curly braces

# Empty dictionary -
d1 = {}
print(d1)
print(type(d1))
print()

# Dictionary with key:value pairs
d2 = {1: 10, 2: 20, 3: 30}
print(d2)
print()

# Diff between sets and dicts ? sets have one value separated by commas
# Dicts have pairs of key:value separated by commas

s3 = {1, 2, 3}
d3 = {1: 10, 2: 20, 3: 30}
print(s3, type(s3), d3, type(d3))
print()

# If key is same, value gets updated. E.g. -> key 4 here
d4 = {1: 10, 2: 20, 3: 30, 4: 400, 4: 40}
print(d4)
print()


# Method 2 : dict comprehension -
d5 = {x: x**2 for x in range(1, 11)}
print(d5)
print()


# Method 3 : dict type constructor dict()
d6 = dict()
print("Empty dict ->", d6)
d7 = dict([('foo', 100), ('bar', 200)])
print(d7)
d8 = dict(foo=100, bar=200)
print(d8)

# Key can only be one, but values can be more than one
students_dict = {'roll_no': [1, 2, 3], 'name': ['naresh', 'suresh', 'ramesh'], 'course': ['python', 'python', 'java']}
print(students_dict)
print()

# Another example
d9 = dict([(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)])
print(d9)
print()

# Creating dictionaries with lists using dict() or zip() :
# 1. Using only dict() -
l1 = [1, 2, 3, 4, 5]
l2 = ['naresh', 'suresh', 'rajesh', 'kishore', 'raman']
l3 = [(l1[i], l2[i]) for i in range(5)]
print(l1)
print(l2)
print(l3)
student_dict = dict(l3)
print(student_dict)
print()

# 2. Using zip(*iterables) and dict() -
# zip() iterates over several iterables in parallel, producing tuples
# with an item from each one. It returns an iterator of tuples where i-th
# tuple contains i-th element from each of the argument iterables/collections.

student_dict2 = dict(zip(l1, l2))
print(student_dict2)
print()

# Eg. 2 :
dict0 = dict(zip("abc", "123"))
print(dict0)

# Eg. 3 :
dict01 = dict(zip(range(1, 6), range(10, 51, 10)))
print(dict01)

# Method 4 : using fromkeys(key[, default])
dict02 = dict.fromkeys("ABCDE", 0)
print(dict02)                   # 0 will be default values for A, B, ...
dict03 = dict.fromkeys(range(10, 51, 10), None)
print(dict03)
dict04 = dict.fromkeys([6, 2, 7, 1, 9], None)
print(dict04)
