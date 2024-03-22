# sum of all even nos between 2 nos.

a = int(input("First number ="))
b = int(input("Second number ="))
sum = 0
while a <= b:
    if a % 2 == 0:
        sum += a
        print(a)
    a += 1
print(f'Sum is {sum}')
