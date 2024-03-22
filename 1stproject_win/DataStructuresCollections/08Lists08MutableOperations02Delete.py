# Collection problems
# LISTS 8
# Mutable Operations 2
# Delete / Remove values
# Keywords - 1. del, 2. remove, 3. clear, 4. pop ( in 09Lists09Stacks and 10Lists10Queues with push/append and del fns )

# 1. del keyword
# Syntax 1 - del list-name[index]           (only for one element)
# Syntax 2 - del list-name[start:stop]      (for one or more elements)
# Syntax 3 - del list-name[start:stop:step] (for one or more elements)

# Example 1 Syntax 1

list1 = list(range(10, 101, 10))
print(list1)
del list1[0]
print(list1)
del list1[-1]
print(list1)
print()

# Example 2 Syntax 2 and 3

print()
list2 = list(range(10, 101, 10))
print(list2)
del list2[:3]
print(list2)
del list2[-3:]
print(list2)
del list2[1:-1]
print(list2)
print()

# remove keyword
# Syntax 1 s.remove(x) - remove first occurrence of item from s where s[i] is equal to x

# Example 3

print()
list3 = [10, 20, 30, 40, 50]
print(list3)
list3.remove(10)
print(list3)
list4 = [10, 20, 30, 40, 10, 20, 30, 40]
print(list4)
list4.remove(30)
print(list4)
print()

# Example 4
# wap to remove values from list

print()
n = int(input("Enter no. of values to the list = "))
list5 = []
for i in range(n):
    num = int(input(f'Enter number {i+1} = '))
    list5.append(num)
print(f'List before editing = {list5}')

n_rem = int(input("From the above list, enter the value to remove = "))
while True:
    if n_rem in list5:
        list5.remove(n_rem)
    else:
        break
print(f'List after editing = {list5}')
print()


# 3. clear keyword
# Syntax -> s.clear() , removes all items from s... similar to del s[:]

# Examples
print()
list6 = [10, 20, 30, 40, 50]
print(list6)
list6.clear()
print(list6)
list7 = [10, 20, 30, 40, 50]
print(list7)
del list7[:]
print(list7)
print()
