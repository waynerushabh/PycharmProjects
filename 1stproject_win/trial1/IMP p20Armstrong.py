# Armstrong number is a^3 + b^3 + c^3 = abc, eg. 153

for num in range(0, 100001):
    num_ori = num2 = num  # 153
    s = num_len = 0  # 0
    while num > 0:
        while num2 != 0:
            num_len += 1  # 1, 2, 3
            num2 = int(num2 // 10)  # 15, 1, 0
        s = s + ((num % 10) ** num_len)  # 3^3, 5^2, 1^3
        num = num // 10  # 15, 1, 0
    if s == num_ori:
        print(f'{num_ori} is an Armstrong Number')
