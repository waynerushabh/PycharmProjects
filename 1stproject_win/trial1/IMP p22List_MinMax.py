# Find Max and Min of a list

x = [2, 3, 1, 3, 9, 4, 23, 12, 45, 43]

min_value = max_value = x[0]

for i in x[1:]:
    if i < min_value:
        min_value = i
    elif i > max_value:
        max_value = i
    else:
        continue

# for i in x[1:]:
#     if i >
    print("Iteration right now : Max and Min are", max_value, min_value)
print("Maximum value is :", max_value)
print("Minimum value is :", min_value)
