# Count the occurrence of all letters of a string
#

def check_freq(x):
    freq = {}                                   # create empty dict
    for i in set(x):                  # check each letter in the string passed by using a set (to remove duplicates)
        freq[i] = x.count(i)          # count letter occurrence in string, assign value to the letter key in dict

# Work here is almost done, but the dict is haphazard. We need to sort it before displaying.

    freq_keys = list(freq.keys())       # create a list of letter keys from the dict
    freq_keys.sort()                    # sort the list
    sorted_freq = {j: freq[j] for j in freq_keys}  # assign the values from the dict to resp letters and make a new dict
    return sorted_freq                  # send the sorted dict


user_string = str(input("Enter any string ="))
print(check_freq(user_string))
