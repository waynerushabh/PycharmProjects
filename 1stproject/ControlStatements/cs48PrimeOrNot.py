# Loop problems
# Prime or not?

num = int(input("Enter a number to check whether it is Prime or not = "))
fac_tors = 0
for i in range(num, 1, -1):
    if num % i == 0:
        fac_tors += 1
if fac_tors > 2:
    print(f'{num} is not a Prime Number.')
else:
    print(f'{num} is a Prime Number.')

print()

# Printing all Prime Numbers till 100

print("Other Prime numbers from first 100 natural numbers are ==>")

for num2 in range(1, 101):
    fac_tors = 0
    for i in range(1, num2+1):
        if num2 % i == 0:
            fac_tors += 1
    if fac_tors < 3:
        print(f'{num2}', " ", end="")
