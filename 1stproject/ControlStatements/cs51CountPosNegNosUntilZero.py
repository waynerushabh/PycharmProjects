# Loop problems
# Count all positive and negative numbers until someone enters zero while entering numbers

num = None
pos_count = neg_count = 0

while num != 0:
    num=int(input("Enter any number = "))
    if num > 0:
        pos_count += 1
    elif num < 0:
        neg_count += 1
print(f'No. of positive integers = {pos_count}\nNo. of negative integers = {neg_count}.')
