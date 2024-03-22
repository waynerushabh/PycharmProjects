def solution(a):
    print(a)
    len_array = len(a)
    print(len_array)
    b = []
    if len_array%2 == 0:
        print("Even")
        for i in range(0, len_array//2):
            b.append(a[i])
            b.append(a[-i-1])
    else:
        print("Odd")
        for i in range(0, len_array//2 + 1):
            b.append(a[i])
            if i != len_array//2:
                b.append(a[-i-1])

    print(b)

    c = sorted(b)
    print(c)
    d = set(c)
    print(d)
    print(len(c), len(d))

    if len(d) != len(c):
        return False
    elif b == c:
        return True
    else:
        return False


listA = [1, 3, 5, 6, 4, 2]
listB = [1, 4, 5, 6, 3]
listC = [-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48]


print(solution(listA))
print("================")
print(solution(listB))
print("================")
print(solution(listC))
