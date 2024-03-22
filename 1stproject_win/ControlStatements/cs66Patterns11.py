# Loop problems
# Pattern 11 - Letter Triangle  A
#                               AB
#                               ABC...

for i in range(65, 91):
    for j in range(65, i+1):
        print(chr(j), " ", end='')
    print()
