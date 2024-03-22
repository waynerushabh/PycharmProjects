# Collection problems
# LISTS 12
# Comprehensions

# Example 1 :
# Create a list by storing squares of all the values from 1 to 20

list1 = []                  # without comprehension
for num in range(1, 21):
    list1.append(num**2)
print(list1)

list2 = [num**2 for num in range(1, 21)]
print(list2)                # using comprehension
print()

# Example 2 :
# WAP to add n integers into a list

print()
n = int(input("Enter no. of Integers to enter = "))
list3 = [int(input("Enter integer = ")) for i in range(n)]
print(list3)                # using comprehension
print()

# Example 3 :
# WAP to create list by storing alphabets from A-Z

print()
list4 = [chr(i) for i in range(65, 91)]
print(list4)                # using comprehension
print()

# Example 4 :
# Odd and Even members of a list

print()
list5 = [4, 2, 7, 8, 3, 6, 4, 5, 9, 12, 13, 16, 17, 18, 19, 23, 35, 37, 67, 54, 56, 34]
even_list5 = [num for num in list5 if num % 2 == 0]
odd_list5 = [num for num in list5 if num % 2 != 0]
print(list5, odd_list5, even_list5, sep="\n")
print()

# Example 5 :
# Names that start with l from a name list

print()
list6_names = ["Lanesra", "Lavanya", "Lorena", "Loredana", "Lana", "Liya", "Mayur", "Mayukh", "Mayuresh", "Reel"]
print(f'Available Names in the pool = {list6_names}')
best_girl_names = [names for names in list6_names if names[0] in "lL"]
print("Best names for our baby girl are =", best_girl_names)
print()

# Example 6 :
# WAP to convert nested list into a sing list (flatten)

print()
list6 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print(list6)
list7 = [value for i in list6 for value in i]
print(list7)
print()
