# Loop problems
# Pattern 14 - Spaces
# 12345
#  2345
#   345....

for i in range(1, 6):
    for j in range(1, 6):
        if j >= i:
            print(j, " ", end='')
        else:
            print("   ", end='')
    print()
