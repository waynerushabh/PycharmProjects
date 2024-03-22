# Loop problems
# Pattern 13 - From given string

str1 = input("Enter a string to see its letter\'s in an decrementing triangle = ")
str_len = len(str1)
for i in range(str_len-1, -1, -1):
    for j in range(0, i+1):
        print(str1[j], " ", end='')
    print()

