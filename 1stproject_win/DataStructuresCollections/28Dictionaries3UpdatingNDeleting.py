# Collection problems
# Dictionaries 3
# Updating and Deleting Dictionaries

# Update
# If key exists, its value is updated
# If key doesn't exist, its value is added.
# Syntax -> dict-name[key] = value

dict1 = {}
print(dict1)
print()

dict1[2000] = 45000                 # Updating using key
dict1[2001] = 55000
dict1[2002] = 65000
dict1[2003] = 75000
print(dict1)
print()

dict1[2000] = 50000                 # Updating using key
print(dict1)
print()


# Delete
# Method 1 : del dict-name[key], gives key error if key not found
d1 = {1: 100, 2: 200, 3: 300, 4: 400, 5: 500}
print(d1)
print()
del d1[2]
print(d1)
print()

# Method 2 : pop(key [, default]), arg 'key' can't be blank, gives value ousted
i = d1.pop(1)
print(d1, i)
print()

# Method 3 : popitem(), uses LIFO order, gives key:value ousted
i = d1.popitem()
print(d1, i)
print()

# Method 4 : clear(), clears all pairs, makes dict empty
d1.clear()
print(d1)
print()
