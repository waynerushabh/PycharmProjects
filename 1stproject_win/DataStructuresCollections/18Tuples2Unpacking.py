# Collection problems
# Tuples 2

# Unpacking Tuples - reading elements from a tuple
# and assigning to multiple variables

# Example 1 :
a = 10, 20, 30
print(a)
x, y, z = a
print(x, y, z)

# Example 2: not an appropriate example
a = 10
b = 20
print(type(a), type(b))
a, b = b, a
print(a, b)
print(type(a), type(b))

# Example 3:
t1 = (10, 20, 30, 40, 50)
print(t1)
a, b, c, d, e = t1
print(a, b, c, d, e)
print()

# Example 4:
# print("Error one")
# x, y, z = t1
# print(x, y, z)

# Example 5:
print()
t2 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
a, b, *c = t2       # variable with * - collection type, takes rest
print(a, b)         # takes remaining values when unpacked & assigned
print()
print(c)
print()
