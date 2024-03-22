# Loop problems
# Keep adding till user says no

ans_wer = "y"
sum_nums = 0
while ans_wer != "n":
    num = int(input("Enter a number to add = "))
    sum_nums += num
    ans_wer = input("Press any key to add another number, Press 'n' to exit sum loop (y/n) = ")
print(f' Sum of all numbers input is {sum_nums}.')
