# Loop programs
# English names of a number's digits
# Eg.- 231 is Two Three One

num = int(input("Enter a number = "))
rev = 0
while num > 0:
    rev = (rev*10) + (num%10)
    num = num // 10

while rev > 0:
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
    else:
        pass
    rev = rev//10

