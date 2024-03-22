# Loop problems
# Pattern 12 - From given string

str1 = input("Enter a string to see its letter\'s in an incrementing triangle = ")
str_len = len(str1)
for i in range(0, str_len):
    for j in range(0, i+1):
        print(str1[j], " ", end='')
    print()
