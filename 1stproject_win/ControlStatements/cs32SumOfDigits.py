# Loop programs
# Sum of digits of input number

ori_num = num = int(input("Enter a number = "))
sum_of_digits = 0
while num != 0:
    sum_of_digits += (num % 10)
    num //= 10
print(f'Sum of {ori_num}\'s digits is {sum_of_digits}.')
