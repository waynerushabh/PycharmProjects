#simple if elif else problems
#ElectricityBill Problem

units_consumed=int(input("Enter the number of units of electricity consumed ="))
if units_consumed<=100:
    print(f' Bill Amount : 0')
elif units_consumed>100 and units_consumed<=200:
    print(f' Bill Amount : {(units_consumed-100)*5}')
elif units_consumed>200:
    print(f' Bill Amount : {((200-100)*5)+((units_consumed-200)*10)}')
else:
    print("Error in Processing. Check your units input and try again.")