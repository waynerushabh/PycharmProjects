# arr = [9, 8, 7, 6, 5] 4
# arr = [10, 10, 10]    0
# arr = [1, 2, 1, 2, 1] 10

# def solution(arr):
#     while True:
#         b = slope_check(arr)


# def upward(ar):
#     u = 0
#     for i in range(0, len(ar)-1):
#         if ar[i] > ar[i+1]:
#             u += 1
#
#
# def downward(ar):
#     d = 0
#     for i in range(0, len(ar)-1):
#         if ar[i] > ar[i+1]:
#             d += 1
#         else:
#             pass
#     return a


arr1 = [9, 8, 7, 6, 5]
arr2 = [10, 10, 10]
arr3 = [1, 2, 1, 2, 1]


def solution(arr):
    print(arr)
    updown = []
    count_cont = 0
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i+1]:
            updown.append("d")
        elif arr[i] < arr[i+1]:
            updown.append("u")
        else:
            pass
        for j in range(0, len(updown) - 1):
            if updown[j] != updown[j+1]:
                print(updown[j], updown[j+1])
                count_cont += 1

    print(len(updown))
    print(updown)
    print(count_cont)


print(solution(arr1))
print("===================")
print(solution(arr2))
print("===================")
print(solution(arr3))
print("===================")
