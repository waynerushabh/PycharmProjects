# To check details

print(" This is not a serious BMI App. Ignore the results if you do not agree. :-) ")

while True:
    name = input("Enter your name = ")
    sex = input("Enter your gender (M/F/O) = ")
    age = input("Enter your age = ")
    weight = input("Enter your weight = ")

    print("Hello, " + name + ".")

    if sex == "M" or sex == "m":
        print("You are Male.")
    elif sex == "F" or sex == "f":
        print("You are Female.")
    elif sex == "O" or sex == "o":
        print("You are non-Binary.")
    else:
        print("Error processing your Gender.")

    if int(age) < 18:
        print("You are underage.")
    elif int(age) < 60:
        print("You are an adult.")
    elif int(age) >= 60:
        print("You are elderly.")
    else:
        print("Error processing your age.")

    if int(weight) >= 78 and sex == "M" or sex == "m":
        print("You are an overweight man.")
    elif int(weight) >= 68 and sex == "F" or sex == "f":
        print("You are an overweight woman.")
    elif int(weight) >= 70:
        print("You are overweight.")
    elif int(weight) <= 48:
        print("You are underweight.")
    else:
        print("No weight issues.")