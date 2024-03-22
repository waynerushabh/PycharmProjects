# Loop Programs (Unusual Question)
# Don't use numbers in input or iteration, but generate this series
# 65 66 67 ..... 90
# We can use ord(ch) to print this series

ch = 'A'
while ch <= 'Z':
    print(ord(ch), "", end='')
    ch = chr(ord(ch) + 1)
