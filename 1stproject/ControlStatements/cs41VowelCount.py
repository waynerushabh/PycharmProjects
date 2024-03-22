# Loop programs
# Count Vowels in a String

str_ip = input("Enter a string to check no. of vowels = ")
vowel_count = 0
for ch in str_ip:
    if ch in "aeiouAEIOU":
        vowel_count += 1
print(f'There are {vowel_count} no. of vowels in {str_ip}')
