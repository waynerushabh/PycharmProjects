# Collection problems
# LISTS 2
# Ways to read a list

# Method 1 -> Indexing
list1 = [10, 20, 30]
print(list1[0])
print(list1[1])
print(list1[2])
print()


# using For loop
list2 = list(range(1, 31, 2))
for i in range(0, 4):
    print(list2[i], " ", end='')
print()


# Function len()
print()
print(len(list1))


# Function append()
list3 = list()
list3.append(10)
list3.append(50)
list3.append(65)
print(list3)



# Another example
# wap to read name and n subject marks, calc total, avg

print()
name = input("Enter Name = ")
n = int(input("Enter number of subjects = "))
marks = []
for i in range(n):
    sub = int(input("Enter Marks = "))
    marks.append(sub)
total = sum(marks)  # Sum inbuilt function
avg = total/n

print(f'Name: {name}')
print(f'Marks : {marks}')
print(f'Total : {total}')
print(f'Avg marks : {avg}')

# Example - wap to read 'n' integers into list, then count even and odd numbers

num_count = int(input("Enter how many numbers to input ? = "))
num_list = []
for i in range(num_count):
    num = int(input(f'Enter number {i+1} = '))
    num_list.append(num)
even_count = odd_count = 0
for i in num_list:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f'List of all numbers = {num_list}')
print(f'Number of even number members = {even_count}')
print(f'Number of odd number members = {odd_count}')
