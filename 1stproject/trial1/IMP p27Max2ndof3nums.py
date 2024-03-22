# Find 2nd maximum of 3 input numbers

n1 = int(input("Enter 1st no. = "))
n2 = int(input("Enter 2nd no. = "))
n3 = int(input("Enter 3rd no. = "))
print(f'{n2} is 2nd maximum') if ((n1 > n2 > n3) or (n3 > n2 > nœ1)) else print(f'{n3} is 2nd maximum') if ((n1 > n3 > n2) or (n2 > n3 > n1)) else print(f'{n1} is 2nd maximum')