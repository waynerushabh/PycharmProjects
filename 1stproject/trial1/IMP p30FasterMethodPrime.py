import time


def prime_num(pass_num):
    primes = [2]

    for number in range(3, pass_num):
        sqrt_number = number ** 0.5

        for factor in primes:
            if number % factor == 0:
                break

            if factor > sqrt_number:
                primes.append(number)
                break

    return primes


def prime_num2(pass_num):
    num = 1
    primes_list = []
    while num <= pass_num:
        i = 1
        factors = 0
        while i <= num:
            if num % i == 0:
                factors += 1
            i += 1
        if factors == 2:
            # print(num, end="\t")
            primes_list.append(num)
        num += 1
    return primes_list


start1 = time.time()
print(prime_num(200))
end1 = time.time()
print("Execution time =", end1 - start1)
print()


start2 = time.time()
print(prime_num2(200))
end2 = time.time()
print("Execution time =", end2 - start2)
