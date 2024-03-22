# Loop Programs
# Count digits of an input number

ori_num = num = int(input("Enter a number = "))
digi_num = 0

while num != 0:
    digi_num = digi_num + 1
    num = num//10
    print(digi_num)
print(f'{ori_num} is a {digi_num} digit number.')
