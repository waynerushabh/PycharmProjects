# simple if elif else problems
# Use nested if
# simple login and password check

# for security, use better names. values input here should be rather taken from forms in real scenario
uname = input("Enter Username : ")
pwd = input("Enter Password : ")

# passwords should have encryption at atleast some level

# simple checks here. real scenario will dictate form values to be checked with database values

if uname == 'ma20361208' or uname == 'MA20361208':
    if pwd == 'Khomesh@18':
        print("You have successfully logged in, Mayuri Meshram.")
    else:
        print("Wrong Password. Try again or Click Forgot Password. \n Passwords are case-sensitive.")
else:
    print("Wrong Username. Please Sign Up if you have not, or check your Username. \n User names are case-sensitive.")