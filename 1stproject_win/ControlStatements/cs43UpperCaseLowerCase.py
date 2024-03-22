# Loop programs
# Convert UpperCase to LowerCase and vice versa

str_ip = input("Enter a string = ")
str_conv = ""
for ch in str_ip:
    if 'a' <= ch <= 'z':
        str_conv += chr(ord(ch)-32)
    else:
        str_conv += ch
print(f'Converted string is {str_conv}.')
