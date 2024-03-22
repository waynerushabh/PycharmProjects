#simple if elif else problems
#input no. is 3 digit or not

#1st approach
num = int(input("Enter the number = "))
if 100<=num<=999:
    print(f'{num} is a 3 digit number.')
else:
    print(f'{num} is not a 3 digit number.')

#2nd approach
num = input("Enter the number again = ")
num_len = len(num)
if num_len==3:
    print(f'{num} is a 3 digit number.')
else:
    print(f'{num} is not a 3 digit number.')