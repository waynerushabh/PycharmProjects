#using def and returning values


def details(name, sex, age, weight):
    print("Hello, " + name + ".")

    if sex == "M":
        print("You are Male.")
    elif sex == "F":
        print("You are Female.")
    elif sex == "O":
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

    if sex == "M" and int(weight) >= 78:
        print("You are an overweight man.")
    elif sex == "F" and int(weight) >= 68:
        print("You are an overweight woman.")
    elif int(weight) >= 70 and not(sex):
        print("You are overweight.")
    elif int(weight) <= 48:
        print("You are underweight.")
    else:
        print("No weight issues.")


def input_fn():
    Name = input("Enter your name = ")
    Sex = input("Enter your gender (M/F/O) = ")
    Age = input("Enter your age = ")
    Weight = input("Enter your weight = ")
    details(Name,Sex,Age,Weight)
    Repeat = input("Do You want to try again? (Y/N) = ")
    if Repeat == 'Y' or Repeat == 'y':
        input_fn()


input_fn()
