# Loop programs
# Proper No. names according to length
# 3,23,45,678 will be 3 crores, 23 lakhs, 45 thousand, 6 hundred and seventy-eight.

ori_num = num = int(input("Enter an amount in Rupees = Rs. "))
rev = 0
num_len = len(str(num))
# print(num_len)

while num > 0:
    rev = (rev*10) + (num % 10)
    num = num // 10

while rev >= 0:
    if rev % 10 == 1:
        print("ONE", " ", end='')
    elif rev % 10 == 2:
        print("TWO", " ", end='')
    elif rev % 10 == 3:
        print("THREE", " ", end='')
    elif rev % 10 == 4:
        print("FOUR", " ", end='')
    elif rev % 10 == 5:
        print("FIVE", " ", end='')
    elif rev % 10 == 6:
        print("SIX", " ", end='')
    elif rev % 10 == 7:
        print("SEVEN", " ", end='')
    elif rev % 10 == 8:
        print("EIGHT", " ", end='')
    elif rev % 10 == 9:
        print("NINE", " ", end='')
    elif rev % 10 == 0:
        print("ZERO", " ", end='')
        continue
    else:
        pass
    rev = rev//10
