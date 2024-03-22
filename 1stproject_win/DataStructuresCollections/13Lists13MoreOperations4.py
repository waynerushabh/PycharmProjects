# Collection problems
# LISTS 13
# More Functions

# len(s) for length of s

list1 = [10, 20, 30, 40, 50]
print("Length of list = ", len(list1))
print()

# min(s) for smallest item in s

print()
print("Smallest item = ", min(list1))
print()

# max(s) for largest item in s

print()
print("Largest item = ", max(list1))

# s.count(x) for occurrences of x in s

print()
print("Occurrence of 20 = ", list1.count(20))
print()

# s.index(x [,i [,j] ] ) for index of first occ. of x in s
# ( at or after index t and before index j)

print()
list2 = [10, 20, 30, 40, 10, 20, 50, 60, 10, 70, 80]
print("List->", list2)
print("Element 20 is at position ->", list2.index(20)+1)
print()

# sorted( iterable, *, key=None, reverse=False )

print()
print(list2)
print("Sorted List ->", sorted(list2))
print("Reverse Sorted ->", sorted(list2, reverse=True))
print()

# any(iterable) - returns true if any iterable is true, else false
# False on empty

print()
list3 = [True, False, True]
print(any(list3))
print()

# all(iterable) - returns true of all iterables are true, else false
# False on empty

print()
list4 = [True, True]
print(all(list4))
print()
