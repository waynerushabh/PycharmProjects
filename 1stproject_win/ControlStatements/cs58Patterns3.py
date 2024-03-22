# Loop problems
# Pattern 3 - Number triangle   1
#                               22
#                               333...

for i in range(1, 6):
    for j in range(1, i+1):
        print(i, " ", end='')
    print()
