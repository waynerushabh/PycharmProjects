# Loop programs
# Prime Number or not

num = int(input("Enter a number = "))
i = 1
factors = 0
while i <= num:
    if num % i == 0:
        factors += 1
    i += 1
if factors > 2:
    print(f'{num} is not a Prime Number.')
else:
    print(f'{num} is a Prime Number.')
