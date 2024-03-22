# Collection problems
# LISTS 11
# More List Operations 3
# Insert, Reverse, Copy (Shallow and Deep), Extend, and Repeat Extend

# Insert -> Syntax - s.insert(i, x) where x is inserted in s at index i ( same as s[i:i] = [x])

list1 = [10, 20, 30, 40, 50]
print(list1)
list1.insert(0, 88)
print(list1)
list1[1:1] = [44, 55, 66]
print(list1)
list1[0:0] = [10, 20, 30, 40]
print(list1)
print()

# Reverse -> Syntax - s.reverse()

print()
list2 = [4, 2, 1, 6, 7, 3, 9, 8]
print(list2)
list2.reverse()
print(list2)
print()

# Shallow Copy -> Syntax - s.copy()
# Shallow copy means - changing original also affects the copy , cause address of original is copied

print()
list3 = [[10, 20], 30]
print("Original list ->", list3, end='')
print()
list3_cp = list3.copy()
print("\nOriginal list ->", list3, end='')
print("\nShallow Copy list ->", list3_cp, end='')
print()
print("\nChanging original list ....\n")
list3[0].append(100)
print("\nOriginal list ->", list3, end='')
print("\nShallow Copy list ->", list3_cp, end='')
print()

# Deep Copy -> Syntax - import copy >>> list-name2 = copy.deepcopy(list-name1)
# Deep copy means - changing original will not affect the copy, as the copy is another instance with same values

import copy

print()
list4 = copy.deepcopy(list3)
print("Original Copy ->", list3)
print("Deep Copy ->", list4)
print()
list3[0].append(99)
print("\nOriginal Copy ->", list3)
print("Deep Copy ->", list4)
print()

# Extend -> Syntax - s.extend(t) or s+=t , where s is extended with contents of t ( just like s[len(s):len(s)] = t )
# can be used to append more than one value

print()
list5 = [10, 20, 30, 40, 50]
print(list5)
list5.append(60)
print("60 appended ->", list5)
print("\nAppend can only extend the list one value at a time.")
print()
print("Although extend can extend more than one value at a time. ")
list5.extend([100, 200, 300])
print("100, 200, 300 extended ->", list5)
print()
print("If we append more than one values somehow, it will append those values as one 'nested' value.")
print()
list5.append([100, 200, 300])
print("100, 200, 300 appended ->", list5)
print()

# Repeated Extend -> Syntax - s *= n, where contents of s are repeated n times

print()
list6 = [10, 20, 30]
print("Original list ->", list6)
list6 *= 3
print("Repeated Extend ->", list6)
print()
