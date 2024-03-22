# Loop problems
# Print sum of the series 1/1!+2/2!+3/3!..... + n/n!

n = int(input("Enter the \'n\'th term to find the sum of series 1/1! + 2/2!... = "))
s = 0
for num in range(1, n+1):
    fact = 1
    for i in range(1, num+1):
        fact = fact * 1
        s = s + num/fact
        print(f'{num}/{fact}', end='')
print(f'={s:.2f}')
