# Loop problems
# Pattern 8 - Number Triangle   1
#                               12
#                               123...

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, " ", end='')
    print()
