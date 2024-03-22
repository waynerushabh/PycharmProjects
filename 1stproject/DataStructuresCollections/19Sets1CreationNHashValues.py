# Collection problems
# SETS 1
# Creation, Empty Sets and Hash Values

# Creation :

# We can't make empty sets with {} method, because {} creates empty dict.
# Method 1 Comma separated within curly braces
# Example 1:
s1 = {10, 20, 30, 40, 50}
print(type(s1))
print(s1)
ss1 = {}
print(ss1)
print(type(ss1))


# Method to make empty sets -
# Method 2 Set comprehension
# Example 2:
print()
s2 = {ch for ch in 'abracadabra' if ch not in 'abcrd'}
print(s2)

# Method to make empty sets -
# Method 3 set() constructor
# Example 3:
print()
s3 = set()
print(s3)
s4 = set('foobar')
print(s4)
s5 = set(['a', 'b', 'foo'])
print(s5)
s6 = set(range(10, 101, 10))
print(s6)
s7 = set("Python")
print(s7)


# Hash Values :

# All immutable objects are hashable objects which can produce hash values.
# ids may be different for 2 same value objects, but their hash values will
# be same.
print()
n1 = 10                 # same value, hash value, and id
n2 = 10
print(n1 == n2)
print(hash(n1))
print(hash(n2))
print(id(n1))
print(id(n2))
print()
f1 = 1.5
f2 = 1.5
print(f1 == f2)
print(hash(f1))
print(hash(f2))
print(id(f1))
print(id(f2))
