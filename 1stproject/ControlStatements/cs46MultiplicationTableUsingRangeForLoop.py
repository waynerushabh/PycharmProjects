# Loop problems
# Print Multiplication Tables of all numbers from 1 to 20

for num in range(1,21):
    for i in range(1,11):
        print(f'{num:2d} X {i:2d} = {num*i:3d}')
    print("==============")
