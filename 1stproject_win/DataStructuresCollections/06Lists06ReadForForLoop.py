# Collection problems
# LISTS 6
# Ways to read a list

# Method 5 -> using for loop, iterables, and append()

# wap to read n integers into list, separate even numbers and odd numbers and store in a different list

num_list = []
even_list = []
odd_list = []
n = int(input("Enter no. of integers you want to store = "))

for i in range(n):
    num = int(input(f'Enter number {i+1} = '))
    num_list.append(num)
print(num_list)
print()

for value in num_list:
    if value % 2 == 0:
        even_list.append(value)
    else:
        odd_list.append(value)
print(num_list, even_list, odd_list, sep="\n")
