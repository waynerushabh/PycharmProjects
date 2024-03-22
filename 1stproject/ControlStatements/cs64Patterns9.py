# Loop problems
# Pattern 9 - Number Triangle   5
#                               54
#                               543...

for i in range(5, 0, -1):
    for j in range(5, i-1, -1):
        print(j, " ", end='')
    print()
