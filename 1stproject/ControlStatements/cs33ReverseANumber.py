# Loop programs
# Reverse a Number using Modulus and Floor

ori_num = num = int(input("Enter a number = "))
rev_num = 0
while num != 0:
    rev_num = (rev_num*10) + (num % 10)
    num = num//10
print(f'Reverse of {ori_num} is {rev_num}')
