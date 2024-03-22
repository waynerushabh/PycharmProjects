# Loop Programs

# first 10 natural nos, whole nos, even nos, odd nos

def natural():
    print("\nFirst 10 Natural numbers = ", " ", end='')
    num = 1
    while num <= 10:
        print(num, " ", end='')
        num += 1


def whole():
    print("\nFirst 10 Whole numbers = ", " ", end='')
    num = 0
    while num <= 10:
        print(num, " ", end='')
        num += 1


def even():
    print("\nFirst 10 Even numbers = ", " ", end='')
    num = 0
    i = 0
    while i < 10:
        num += 2
        i += 1
        print(num, " ", end='')


def odd():
    print("\nFirst 10 Odd numbers = ", " ", end='')
    num = -1
    i = 0
    while i < 10:
        num += 2
        i += 1
        print(num, " ", end='')


natural()
whole()
even()
odd()
