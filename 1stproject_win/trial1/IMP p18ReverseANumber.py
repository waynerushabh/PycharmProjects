# Reverse a Number

num = int(input("Enter any number ="))
reversenum = 0

while num > 0:
    r = num % 10
    reversenum = (reversenum*10)+r
    num = num//10
print(f'Reverse number is {reversenum}')