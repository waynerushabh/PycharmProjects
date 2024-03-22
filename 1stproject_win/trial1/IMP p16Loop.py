# Length of number without using len

n = int(input("Enter any number ="))
c = 0
while n != 0:
    c += 1
    n = int(n/10)
print(f'Length of number is {c}')