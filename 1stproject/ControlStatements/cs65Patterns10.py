# Loop problems
# Pattern 10 - Number Triangle  54321
#                               5432
#                               543...

for i in range(1, 6):
    for j in range(5, i-1, -1):
        print(j, " ", end='')
    print()
