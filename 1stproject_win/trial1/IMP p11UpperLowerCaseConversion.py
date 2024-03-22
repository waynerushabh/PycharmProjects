# Uppercase Lowercase ViceVersa


while True:
    ch = input("Enter any single letter only = ")
    if 'a' <= ch <= 'z':
        n = ord(ch)
        n -= 32
        ch = chr(n)
        print(ch)
    elif 'A' <= ch <= 'Z':
        n = ord(ch)
        n += 32
        ch = chr(n)
        print(ch)
    else:
        print("Invalid Input. Input should be a single letter from the alphabet range.")
