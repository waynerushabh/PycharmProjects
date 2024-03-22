# Loop Programs
# Find sum of all even numbers between two different input nos

aa = a = int(input("Enter lower no. = "))
b = int(input("Enter higher no. = "))
sum_of_even = 0
while a < b:
    if a%2 == 0:
        sum_of_even += a
    a += 1
print(f'Sum of all even numbers between {aa} and {b} is {sum_of_even}.')
