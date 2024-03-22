# Loop problems
# Pattern 5 - Number triangle   5
#                               44
#                               333...

for i in range(5, 0, -1):
    for j in range(5, i-1, -1):
        print(i, " ", end='')
    print()
