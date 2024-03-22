#simple if elif else problems
#Calculate RoadTax according to costprice of the bike

bike_cp = int(input("Enter the price of your bike = "))

if 0 <= bike_cp <= 50000:
    bike_tax = (5/100)*bike_cp
    print(f'Your Road Tax : Rs. {bike_tax:.2f}')
elif bike_cp <= 100000:
    bike_tax = (10/100)*bike_cp
    print(f'Your Road Tax : Rs. {bike_tax:.2f}')
elif bike_cp > 100000:
    bike_tax = (15/100)*bike_cp
    print(f'Your Road Tax : Rs. {bike_tax:.2f}')
else:
    print("Error Processing. Try again with correct price of your bike.")