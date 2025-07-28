# Collection problems
# LISTS 7
# Mutable Operations 1
# Update / Replace Values
# Syntax 1 - s[i] = x, where item at i index is replaced by x... Note : if index out of range, then error.
# Syntax 2 - s[i:j] = t, where slice of s from i-j is replaced by contents of t iterable. Note: includes if out of range
# Syntax 3 - s[i:j:k] = t, where elements of s[i:j:k] are replaced by those of t iterable. Note: incl. if out of range

# Example 1

list1 = [10, 20, 30, 40, 50]
list1[0] = 99
print(list1)
list1[-1] = 88
print(list1)
list1[3] = 77
print(list1)
print()

# Example 2
# Very Important
# wap to sort the elements of list in ascending order using bubble sort

print()
n = int(input("Enter no. of values to input = "))
list2 = []
for i in range(n):
    num = int(input(f'Enter number {i+1}= '))
    list2.append(num)
print(f'Before Sorting = {list2}')

for i in range(n):
    for j in range(0, n-1):
        if list2[j] > list2[j+1]:
            list2[j], list2[j+1] = list2[j+1], list2[j]

print(f'After Sorting = {list2}')
print()

# Example 3

print()
list3 = list(range(10, 101, 10))
print(list3)
list3[1::2] = [11, 22, 33, 44, 55]
print(list3)
list3[10:] = [99, 77]
print(list3)
list3[20:] = [71, 89]
print(list3)
print()
