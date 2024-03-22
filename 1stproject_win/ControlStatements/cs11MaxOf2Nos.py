#simple if elif else problems
#Maximum of two numbers

n1, n2 = map(int,input("Enter two numbers, separate by comma = ").split(","))
if n1>n2:
    print(f'{n1} is maximum.')
else:
    print(f'{n2} is maximum.')