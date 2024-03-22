# Leetcode
a = [75, 61, 32, 15, 10, 9, 7, 1]
n = 26
# -> 15+10+1, 10+9+7
# Find out the array element set which makes the sum of given input.
# For example Array = [75,61,32,15,10,9,7,1] and input = 26
# Output = Sum of 26 is [{15+10+1}, {10+9+7}]
import itertools


def tuple_to_string(passed_list: list) -> str:
    return_string = "{"
    for num in passed_list:
        return_string += f" {num} "
    return_string += "}"
    return return_string


def find_sum(passed_list: list, target: int) -> str:
    return_list = []
    array_comb = [list(itertools.combinations(passed_list, i + 1)) for i in range(len(passed_list))]

    sub_arrays = [inside for inside1 in array_comb for inside in inside1]
    # print(sub_arrays)

    for sub_array in sub_arrays:
        sum_sub_array = 0
        for element in sub_array:
            sum_sub_array += element
        if sum_sub_array == target:
            return_list.append(tuple_to_string(sub_array))

    for tups in return_list:
        print(tups, end=', ')


find_sum(a, n)

##########################
# Tried to solve one Wordscape problem (longest word was gainer), at Level 388
# Can be reused again for different word arrangements
print()
print("===============", end='\n\n')
letters = [i for i in 'gainer']
print(letters)

perm = itertools.permutations(letters, 6)
print(perm)

for i in perm:
    if i[0] == 'r':
        print(''.join(i), end = "\n\n")
