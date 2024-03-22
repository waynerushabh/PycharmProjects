# Loop programs
# Palindrome number or not?

ori_num = num = int(input("Enter a number = "))
rev_num = 0
while num != 0:
    rev_num = (rev_num*10) + (num % 10)
    num //= 10
print(f'Reverse of {ori_num} is {rev_num}.')
if ori_num == rev_num:
    print(f'{ori_num} is a palindrome number.')
else:
    print(f'{ori_num} is not a palindrome number.')
