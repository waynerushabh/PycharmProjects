# Collection problems
# SETS 3
# Adding and Removing elements to/from Set

# Adding using add(element)
# Example 1
print()
s1 = set()
n = int(input("Enter no. of values to enter = "))
for i in range(n):
    ele = input(f'Enter element {i+1} = ')
    s1.add(ele)
for val in s1:
    print(f'{val}')

# Example 2
print()
set1 = set()
n = int(input("Enter no. of countries = "))
for i in range(n):
    countries = input(f'Enter country {i+1} : ')
    set1.add(countries)
print(len(countries)-1)
print(set1)

# Removing methods - remove, discard, pop, clear

# Method 1 - remove(element), error if not present
print()
s2 = {10, 20, 30, 40, 50}
print("Original Set ->", s2)
s2.remove(30)
print("Removed Element 30 Set ->", s2)
# s2.remove(60)                               # Should give an error
# print("Removed Element 60 Set ->", s2)      # Should give an error

# Method 2 - discard(element), ignores if not present
print()
s3 = {10, 20, 30, 40, 50}
print("Original Set ->", s3)
s3.discard(10)
print("Removed Element 10 Set ->", s3)
s3.discard(10)
print("Trying again to remove 10 ->", s3)

# Method 3 - pop() , will be arbitrary as sets don't have ordered sequence
print()
s4 = {10, 20, 30, 40, 50}
print("Original Set ->", s4)
s4.pop()
print("After pop ->", s4)
s4.pop()
print("After pop again ->", s4)
print()

# Method 4 - clear(), for removing all elements
print()
s4.clear()
print("Clearing Set ->", s4)
