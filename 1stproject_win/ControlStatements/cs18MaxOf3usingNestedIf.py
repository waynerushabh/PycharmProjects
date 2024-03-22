# simple if elif else problems
# Find max of 3 nos. using nested if

n1 , n2 , n3 = map(int, input("Enter 3 numbers to compare, separate with commas").split(","))
if n1>n2:
    if n1>n3:
        print(f'{n1} is maximum.')  # since n1>n2,n3
    else:
        print(f'{n3} is maximum.')  # since n3>n1>n2
elif n2>n3:
    print(f'{n2} is maximum.')  # since n2>n1,n3
else:
    print(f'{n3} is maximum.')  # since n3>n2>n1
