# Loop programs
# Input number is Armstrong Number or not
# Armstrong number is a^3 + b^3 + c^3 +.... = (abc...)... eg. 153

ori_num = num = int(input("Enter a number = "))
sum_of_cubes = 0
while num > 0 or num < 0:
    sum_of_cubes = sum_of_cubes + ((num % 10) ** 3)
    num = num//10
if sum_of_cubes == ori_num:
    print(f'{ori_num} is an Armstrong Number.')
else:
    print(f'{ori_num} is not an Armstrong Number.')
