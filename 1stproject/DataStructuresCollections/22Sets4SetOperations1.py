# Collection problems
# SETS 4
# Set Operations 1

# Union - all elements of set1 | set2 | .....
a1 = {10, 20, 30}
b1 = {300, 400, 500}
c1 = a1 | b1                # 1st method
c2 = a1.union(b1)           # 2nd method
print(c1)
print(c2)

# Intersection - common elements of set1 & set2 & .....
print()
s1 = {10, 20, 30, 40, 50, 60, 70}
s2 = {10, 20, 30}
s3 = s1 & s2
s4 = s1.intersection(s2)
print(s3)
print(s4)
print()

# difference - all uncommon elements of only set1  -> - set2 - ...
print()
set1 = {100, 300, 400, 200, 500, 600}
set2 = {100, 200, 700}
set3 = set1 - set2
set4 = set1.difference(set2)
print(set3)
print(set4)

# symmetric difference - only uncommon elements of all set1 and set2 and... -> set1 ^ set2 ^ .....
print()
a = {100, 200, 300}
b = {100, 400, 500}
c = a ^ b
d = a.symmetric_difference(b)
print(c)
print(d)

# copy - shallow copy of set1
print()
ori_set = {100, 200, 300}
copy_set = ori_set.copy()
print(ori_set)
print(copy_set)
print()

# update(*others) set1 |= set2 |.... Also called union update.
print()
ru = {1, 2, 3, 4, 5}
ma = {6, 7, 8, 9}
maru = ru.union(ma)
print(maru)
ru.update(ma)
print(ru)
ru |= ma
print(ru)

# intersection update - set1 &= set2 &= ....
print()
rush = {1, 2, 3, 4, 5}
mayu = {1, 2}
rush.intersection_update(mayu)
print(rush)
rush &= mayu
print(rush)

# difference update - set1 -= set2 -= .....
print()
ru1 = {1, 2, 3, 4, 5}
ma1 = {1, 2, 3}
ru1 -= ma1
print(ru1)
ru1.difference_update(ma1)
print(ru1)

# symmetric difference update - set1 ^= set2 ^= .....
print()
rush1 = {1, 2, 3, 4, 5}
mayu1 = {3, 4, 5, 6, 7}
rush1 ^= mayu1
print(rush1)
rush1.symmetric_difference_update(mayu1)
print(rush1)
