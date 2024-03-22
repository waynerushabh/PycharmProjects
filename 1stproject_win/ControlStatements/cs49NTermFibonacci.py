# Loop problems
# Fibonacci series till nth term

num = int(input("Enter Fibonacci Series \'n\'th term = "))
a = 0
b = 1
print(a, "", b, " ", end='')
s = 0
for i in range(num-2):
    s = a + b
    print(s, " ", end='')
    a = b
    b = s
