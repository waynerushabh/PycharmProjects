list1 = [1, 2, 3, 4.5, "abc", True]

for i in list1:
    if type(i) in [int, float]:
        print(i)

print('-------')

for i in list1:
    if type(i) is int:
        print(i)

