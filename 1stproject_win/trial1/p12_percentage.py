# Percentage Grade program - 90< A, 80-90 B, 60-80 C, 60> D

percent = float(input("Enter the percentage ="))

if percent > 90:
    print("Grade : A")
elif 80 < percent <= 90:
    print("Grade : B")
elif 60 <= percent <= 80:
    print("Grade : C")
elif percent < 60:
    print("Grade : D")
else:
    print("Error Evaluating")
