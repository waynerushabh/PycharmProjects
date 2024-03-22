# Loop problems
# Enter unlimited numbers and count their average
ans_wer = 'y'
total_sum = count = 0
while ans_wer != 'n':
    num = float(input("Add another number = "))
    total_sum += num
    count += 1
    ans_wer = input("Press 'y' to add another number OR 'n' to find the average (y/n) = ")
print(f'Average of all input numbers is {(total_sum/count):.2f}')
