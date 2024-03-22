# Sum of Digits

num = int(input("Enter any number ="))  # 1234
s = 0
while num > 0:
    i = num % 10
    s += i
    num = num//10
print("Sum is =", s)
