#simple if elif else problems
#Leap Year or not

yr=int(input("Enter any year = "))
if yr%4==00 and (yr%100!=0 or yr%400==0):
    print(f'{yr} is a Leap Year.')
else:
    print(f'{yr} is not a Leap Year.')
