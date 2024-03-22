# Palindrome number

num = int(input("Enter any number = "))
num_ori = num
num_rev = 0
while num > 0:
    r = num % 10
    num_rev = (num_rev * 10) + r
    num = num//10
print(f'Reverse number is= {num_rev}')

if num_rev == num_ori:
    print("Entered number is a palindrome")
else:
    print("Entered number is not a palindrome")
