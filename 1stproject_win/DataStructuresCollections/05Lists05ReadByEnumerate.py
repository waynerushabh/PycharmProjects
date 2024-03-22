# Collection problems
# LISTS 5
# Ways to read a list

# Method 4 -> Enumerate ( By using enumerate(iterable, start=0) and next(x) function ( or rather print(next(x)) )
# Similar to Iterator, cause it needs iterable and it is read-only.
# Different from Iterator only cause it returns start n value
# So it can be used to generate pair value, like in dictionaries. Can also convert lists to dictionaries.

# Example 1

list1 = [10, 20, 30, 40, 50]
e = enumerate(list1)
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print()
print(list1)
print()

# Example 2, changing key for same values from Example 1 - list1

print()
e1 = enumerate(list1, start=200)
print(next(e1))
print(next(e1))
print(next(e1))
print(next(e1))
print(next(e1))
print()

# Example 3

print()
scores_list = [40, 50, 20, 30, 10, 60]
e = enumerate(scores_list, start=1)
for p in e:
    print(next(e))
    print()
    print(p)

print()
