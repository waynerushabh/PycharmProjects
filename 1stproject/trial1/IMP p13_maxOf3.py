# Single input, Maximum of three numbers

n1, n2, n3 = map(int, input("Enter 3 numbers and give space after each one =").split(" "))
print("The numbers are =", n1, n2, n3)

if n1 > n2:
    if n1 > n3:
        print(f'{n1} is maximum')
    else:
        print(f'{n3} is maximum')
elif n2 > n3:
    print(f'{n2} is maximum')
else:
    print(f'{n3} is maximum')