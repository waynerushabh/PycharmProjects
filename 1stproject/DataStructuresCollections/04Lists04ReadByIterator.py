# Collection problems
# LISTS 4
# Ways to read a list

# Method 3 -> Iterators ( using x = iter(iterable) syntax and next(x) function)
# Useful in non index based collections.
# Note : they are read-only. no modification allowed.


# Example 1

list1 = list(range(10, 51, 10))
print(list1)
x = iter(list1)
value1 = next(x)
value2 = next(x)
value3 = next(x)
value4 = next(x)
value5 = next(x)
print(value1, value2, value3, value4, value5, sep=", ")
print()

# Example 2, more practical

print()
list1 = list(range(10, 101, 10))
print(list1)
print()
print(len(list1))
print()
x = iter(list1)
for value in x:
    next(x)
    print(value, end=' ')
