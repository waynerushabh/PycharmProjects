# Loop Programs
# Multiplication Tables of first 20 natural numbers

num = 1
while num <= 20:  # numbers up to 20 loop
    i = 1
    while i <= 10:  # 1-10 multiplication factors
        print(f'{num:2d} X {i:2d} = {num*i:3d}')
        i += 1
    num += 1
    print("=============")
