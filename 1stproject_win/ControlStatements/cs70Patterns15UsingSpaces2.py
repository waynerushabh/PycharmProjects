# Loop problems
# Pattern 15 - Spaces
#     1
#    21
#   321....

for i in range(1, 6):
    for j in range(5, 0, -1):
        if j <= i:
            print(j, " ", end='')
        else:
            print("   ", end='')
    print()
