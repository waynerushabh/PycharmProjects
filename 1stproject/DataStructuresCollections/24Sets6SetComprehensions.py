# Collection problems
# SETS 6
# Set Comprehensions

# Syntax 1 - {expression for variable in iterable}
# Syntax 2 - {expression for variable in iterable if condition}
# Syntax 3 - {expression for variable in iterable for variable in iterable}

# Syntax 1 -
# without comprehension
set1 = set()
for n in range(1, 11):
    set1.add(n**2)
print(set1)

# with comprehension
print()
set2 = {num**2 for num in range(1, 11)}
print(set2)


# WAP to add n names into set
print()
n = int(input("Enter no. of Names to enter = "))
names_set = set()
names_set1 = set()
# without comprehension
for i in range(n):
    name = input(f'Enter name {i+1} = ')
    names_set.add(name)
print()
print(f'Names list = {names_set}')
print()
# with comprehension
names_set1 = {input(f'Enter name {i+1} = ') for i in range(n)}
print(f'Names List = {names_set1}')

# Syntax 2 :
print()
set1 = {1, 6, 9, 4, 6, 3, 8, 3, 88, 44, 33, 23, 54}
print(set1)
set2_even = {num for num in set1 if num %2 == 0}
set2_odd = {num for num in set1 if num %2 != 0}
print(set2_odd)
print(set2_even)
print()