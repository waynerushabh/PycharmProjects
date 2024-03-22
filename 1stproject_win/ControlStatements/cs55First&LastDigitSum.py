# Loop problems
# Sum of first and last digit of a number

num = input("Enter a number = ")
num_len = len(num)-1
first = int(num)//10**num_len
last = int(num) % 10
print("Sum of First and Last digits is = ", first+last)
