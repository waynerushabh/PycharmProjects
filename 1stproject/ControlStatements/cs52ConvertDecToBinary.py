# Loop problems
# Convert Decimal to Binary

ori_num = num = int(input("Enter a number to convert it into Binary = "))
bin_num = 0
p = 1
while num > 0:
    r = num % 2
    bin_num += (r*p)
    p = p*10
    num //= 2
print(f'Binary of {ori_num} is {bin_num}.')
