# Loop Programs
# Print All ASCII codes
# We can start from num=0 but visible codes start from 33

num = 33
while num < 128:  # limit of ASCII among Unicode is 127
    print(chr(num), "", end='')
    num += 1
