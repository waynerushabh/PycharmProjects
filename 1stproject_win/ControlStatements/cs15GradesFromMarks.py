#simple if elif else problems
#Enter Marks to Find Grades

percent = int(input("Enter your total annual percentage = "))
if 90 < percent <= 100:
    print("Grade A")
elif percent > 80:
    print("Grade B")
elif percent >= 60:
    print("Grade C")
elif percent >= 0:
    print("Grade D")
else:
    print("Error computing. Try again.")