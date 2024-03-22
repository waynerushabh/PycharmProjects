# Loop problems
# Pattern 4 - Number triangle   55555
#                               4444
#                               333...

for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(i, " ", end='')
    print()

# Another Method

print()
for r in range(5, 0, -1):
    for c in range(r, 0, -1):
        print(r, " ", end='')
    print()
