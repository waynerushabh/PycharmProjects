# Loop problems
# Pattern 16 - Spaces
#     5
#    45
#   345....

for i in range(5, 0, -1):
    for j in range(1, 6):
        if j >= i:
            print(j, " ", end='')
        else:
            print("   ", end='')
    print()
