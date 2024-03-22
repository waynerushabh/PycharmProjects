# Loop Control Statements - Jump Control Statements like break, continue and else
# Review for pass, return, etc. later

# Break -> wap to print sum of first 20 even numbers

even_num_count = 0
even_num_sum = 0
num = 1
while True:
    if num % 2 == 0:
        even_num_sum += num
        even_num_count += 1
    num += 1
    if even_num_count == 20 :
        break
print(f'Sum of first 20 even numbers is {even_num_sum}.')

# Break -> wap to find input no. is prime

num = int(input("Enter any number to check whether it\'s Prime = "))
fact_count = 0
for fact in range(1, num+1):
    if num % fact == 0:
        fact_count += 1
    if fact_count>2:
        break
if fact_count == 2:
    print(f'{num} is a Prime Number.')
else:
    print(f'{num} is not a Prime Number.')

# Else -> While Else

num = 1
while num <= 10:
    print(num)
    num += 1
    if num > 5:
        break
else:
    print("Else Block")

# Else -> For Else

for num in range(1, 11):
    print(num)
    if num > 5:
        break
else:
    print("Else Block")

# Continue ->

for num in range(1, 11):
    if num % 2 != 0:
        continue
    print(num)
