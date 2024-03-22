# Loop programs
# Count all letters, numbers and special characters in a string

str_ip = input("Enter a string = ")
alpha_bets = num_bers = spec_chars = 0

for ch in str_ip:
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        alpha_bets += 1
    elif ('0' <= ch <= '9'):
        num_bers += 1
    else:
        spec_chars += 1
print(f'There are {alpha_bets} letters from the alphabet, {num_bers} numerals, and {spec_chars} special characters.')
