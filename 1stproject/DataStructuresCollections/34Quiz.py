# Q1

list_a = [1, 2, 3]
list_b = list_a[-2:-1]
list_c = list_a[-1:-2]

print(list_b)
print(list_c)

# Q2

temp_list = [1, 2, 3]
for i in range(len(temp_list)):
    temp_list.insert(i, 0)
print(temp_list)

# Q3

orig_list = [1, 2, 3]
new_list = orig_list
del new_list[1:2]

print(len(orig_list), len(new_list))

# Q4

my_numbers = [[i for i in range(3)] for j in range(4)]
print(my_numbers)

# Q5

values = [[3 - x for x in range(2)] for y in range(5)]

sum = 0.0
for row in values:
    for cell in row:
        sum += cell

print(sum)

# Q6

ratings = [3.0, 4.5, 6.3, 4.5, 6.7]
print(ratings[-2:-4])

# Q7

my_vals = [1, 2, 3, 4, 5]
my_vals[1], my_vals[2] = my_vals[2], my_vals[1]
print(my_vals)

# Q8

my_list = [0, 1, 2] * 3 + [0]
print(len(my_list))
print(my_list)

# Q9

vals = (1, 2, 3, 4)
vals = vals[1:-1]
vals = vals[1]
print(vals)

# Q10

tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[1]
print(tup)

# Q11

list1 = [1, 2, 3]
list2 = list1[-3:-1]
print(list1, list2)

# Q12

print(1 | 0 ^ 1 & ~0)

# Q13

x = 4
y = 5
z = 3
print(x == y or z)

# Q14

for i in range(2):
        print ('%')
else:
        print('%')

# Q15

x = [
    'a',
    'b',
    {
        'one': 1,
        'two':
        {
            'x' : 10,
            'y' : 20,
            'z' : 30
        },
        'three': 3
    },
    'c',
    'd'
]
print(30 in x[2])

list1 = range(3)
for i in list1:
    print(i)