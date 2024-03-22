# Loop problems
# Pattern 18 - Strings and Spaces
#   PYTHON
#    YTHON
#     THON....

str1 = input("Enter a String to slowly diminish it from the first letter = ")
str_len = len(str1)
for i in range(0, str_len):
    for j in range(0, str_len):
        if j >= i:
            print(str1[j], " ", end='')
        else:
            print("   ", end='')
    print()
