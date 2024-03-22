# Collection problems
# Tuples 2
# Reading Tuples

# 1. Using Index -

country = ("Spain", "Italy", "India", "England", "Germany", "France", "Portugal")
print(country[1])
print(country[2])
print(country[0])
print(country[-1])
print()

# 2. Using Value -

print()
for name in country:
    print(name)
print()
if "Russia" not in country:
    print("Russia is not a recognised member in this collection.")
print()

# 3. Slicing/ range of index -

print()
print(country[3:5])
print()
print(country[-7:-3])
print()
print(country[0:7:1])
print()
print(country[::])
print()
