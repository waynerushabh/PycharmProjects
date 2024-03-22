# Collection problems
# SETS 2
# Reading Sets

# Methods to read Sets :

# Since Sets are non-index collections, we can not read using index and slicing.
# Other ways are by iterator, enumerator, or for loop.

# Method 1 : Iterator
# Example 1 :
s1 = {10, 20, 30, 40, 50}
i = iter(s1)
a = next(i)
b = next(i)
c = next(i)
d = next(i)
e = next(i)
print(a, b, c, d, e)

# Example 2:
print()
s2 = set(range(10, 101, 10))
i = iter(s2)
for x in i:
    print(x)

# Method 2 : Enumerate
print()
s3 = set(range(10, 101, 10))
e = enumerate(s3)
for x in e:
    print(x)

# Method 3 : For Loop
print()
s4 = set(range(10, 101, 10))
for i in s4:
    print(i)
