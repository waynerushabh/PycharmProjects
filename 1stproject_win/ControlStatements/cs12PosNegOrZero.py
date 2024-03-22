#simple if elif else problems
#Number is positive, negative or zero? Check

num=int(input("Enter any integer = "))
if num>0:
    print(f'{num} is positive.')
elif num<0:
    print(f'{num} is negative.')
elif num==0:
    print(f'{num} is zero.')
else:
    print(f'{num} error processing integer. Try Again.')