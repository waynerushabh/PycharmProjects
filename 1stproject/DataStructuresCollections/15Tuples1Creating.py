# Collection problems
# Tuples 1
# Creating Tuples

# Creating Empty Tuples :
tup1 = ()
print(type(tup1))
print(tup1)

# singleton tuple using a, or (a,)
tup2 = 34,
tup3 = (34,)
print(type(tup2), type(tup3))
print(tup2, tup3)
print()

# separating items with commas a, b, c or (a, b, c)
tup4 = 10, 20, 30
tup5 = (10, 20, 30)
print(type(tup4), type(tup5))
print(tup4, tup5)
print()

# using tuple() constructor :
tup6 = tuple()
print(type(tup6))
print(tup6)

# using tuple(iterable) constructor
tup7 = tuple(range(1, 11, 1))
print(type(tup7))
print(tup7)
