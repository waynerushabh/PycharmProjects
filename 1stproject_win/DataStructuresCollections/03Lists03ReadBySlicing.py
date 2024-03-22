# Collection problems
# LISTS 3
# Ways to read a list

# Method 2 -> Slicing ( Slicing can affect more values, indexing affects only one value at a time )

# Using Slice Operator -> list-name[start:stop:step] and many more related syntax

# Syntax 1 -> [start:stop:step]

list1 = list(range(10, 101, 10))
print(list1)
list2 = list1[0:5]
print(list2)
list3 = list1[5:10:1]
print(list3)
list4 = list1[0:10:2]
print(list4)
list5 = list1[-1:-11:-1]
print(list5)
list6 = list1[-1:-11:-3]
print(list6)
print()

# Syntax 2 -> list-name[::step]

l1 = list(range(10, 101, 10))
print(l1)
l2 = l1[::1]
print(l2)
l3 = l1[::2]
print(l3)
l4 = l1[::-1]
print(l4)
l5 = l1[::-2]
print(l5)
print()

# Syntax 3 -> list-name[start:]

print()
ls1 = list(range(1, 21, 2))
print(ls1)
ls2 = ls1[0:]
print(ls2)
ls3 = ls1[5:]
print(ls3)
ls4 = ls1[-4:]
print(ls4)
print()

# Syntax 4 -> list-name[start:stop]

print()
col1 = list(range(1, 21, 2))
print(col1)
col2 = col1[0:4]
print(col2)
col3 = col1[0:-2]
print(col3)
col4 = col1[-3:-1]
print(col4)
print()

# Syntax 5 -> list-name[:stop:] or list-name[:stop]

print()
lsi1 = list(range(1, 31, 3))
print(lsi1)
lsi2 = lsi1[:5:]
print(lsi2)
lsi3 = lsi1[:5]
print(lsi3)
lsi4 = lsi1[:-3]
print(lsi4)
print()

# Syntax 6 -> list-name[::] or list-name[:] , no values means entire list

print()
lists1 = list(range(10, 101, 10))
print(lists1)
lists2 = lists1[::]
print(lists2)
lists3 = lists1[:]
print(lists3)
lists4 = lists1[::-1]  # Syntax 2 example
print(lists4)
print()

# Using sort function, by sort(*, key=None, reverse=False)

print()
List1 = [4, 1, 5, 6, 7]
print(List1)
List1.sort()
print(List1)
List1.sort(reverse=True)
print(List1)
List2 = ['B', 'a', 'D', 'A', 'b']
print(List2)
List2.sort()
print(List2)
List2.sort(reverse=True)
print(List2)
List2.sort(key=str.upper)  # Will consider all as uppercase
print(List2)
print()

# Using Slice Object and function
# Syntax slice(stop) or slice(start, stop, step)

# Examples -

print()
ori_list = list(range(10, 101, 10))
s1 = slice(0, 3)
sliced_list = ori_list[s1]
print(ori_list)
print(sliced_list)
s2 = slice(5)
sliced_list = ori_list[s2]
print(sliced_list)
s3 = slice(-1, -11, -1)
sliced_list = ori_list[s3]
print(sliced_list)
print()
