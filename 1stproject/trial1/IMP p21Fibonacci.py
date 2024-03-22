# Fibonacci Series till 1000

a = 0
b = 1
print(f'  {a}')
print(f', {b}')
s = 0

while s < 1000:
    s = a+b
    a = b
    b = s
    print(f', {s}')
