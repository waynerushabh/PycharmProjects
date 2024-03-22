# Find Max (highest) and Second highest of a list

x = [2, 3, 1, 3, 9, 4, 23, 12, 45, 43]

sec_high = max_value = x[0]
for i in x[1:]:
    if i > max_value or i > sec_high:
        if i > max_value:
            sec_high = max_value
            max_value = i
        else:
            sec_high = i
    print("Iteration right now : Max and 2nd highest are", max_value, sec_high)
print("Maximum value is :", max_value)
