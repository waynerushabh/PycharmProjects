while True:
    a = int(input("Enter first number = "))
    b = int(input("Enter second number = "))
    calc = input("Enter operation (+,-,*,/) = ")
    if calc == "+":
        print(a+b)
    elif calc == "-":
        print(a-b)
    elif calc == "*":
        print(a*b)
    elif calc == "/":
        print(a/b)
    else:
        print("Invalid Operation")
        break

