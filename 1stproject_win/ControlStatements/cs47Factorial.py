# Loop problems
# Factorial of input number

num = int(input("Enter number to find its factorial = "))
fact_o_rial = 1
for i in range(num, 0, -1):
    fact_o_rial *= i
print(f'Factorial = {fact_o_rial}')

