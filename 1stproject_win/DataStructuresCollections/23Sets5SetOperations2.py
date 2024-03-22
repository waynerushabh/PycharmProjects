# Collection problems
# SETS 5
# Set Examination Operators

# isdisjoint
s1 = set(range(10, 51, 10))
s2 = set(range(60, 101, 10))
s3 = set(range(10, 101, 10))
print(s1, s2, s3)
print(s3.isdisjoint(s1))
print(s3.isdisjoint(s2))
print(s1.isdisjoint(s2))

# issubset or <=
print()
print(s1.issubset(s3))
print(s3.issubset(s2))
print(s1 <= s3)

# issuperset or >=
print()
print(s3.issuperset(s2))
print(s1.issuperset(s3))
print(s3 >= s2)
