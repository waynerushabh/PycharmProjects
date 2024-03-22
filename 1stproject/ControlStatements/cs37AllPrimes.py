# Loop programs
# Prime Numbers List until 1000

num = 1
while num <= 1000:
    i = 1
    factors = 0
    while i <= num:
        if num % i == 0:
            factors += 1
        i += 1
    if factors == 2:
        print(num, end="\t")
    num += 1
