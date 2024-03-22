# Loop problems
# Pattern 17 - Spaces
# 012345
#  12345
#   2345....

for i in range(0, 6):
    for j in range(0, 6):
        if j >= i:
            print(j, " ", end='')
        else:
            print("   ", end='')
    print()
