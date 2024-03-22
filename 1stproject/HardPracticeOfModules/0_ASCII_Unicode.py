# Practicing Devanagari scripts

# print(chr(int(0x0900)))
# print(chr(int(0x097F)))
# print(chr(int(0xA8E0)))
# print(chr(int(0xA8FF)))
# print(chr(int(0x11B00)))
# print(chr(int(0x11B5F)))
# print(chr(int(0x1CD0)))
# print(chr(int(0x1CFF)))

for i in range(int(0x0900), int(0x097F)+ 100):
    print(str(i) + ' : ' + chr(i))
print('=================')
# for i in range(int(0xA8E0), int(0xA8FF)+1):
#     print(str(i) + ' : ' + chr(i))
# print('=================')
# for i in range(int(0x11B00), int(0x11B5F)+1):
#     print(str(i) + ' : ' + chr(i))
# print('=================')
# for i in range(int(0x1CD0), int(0x1CFF)+1):
#     print(str(i) + ' : ' + chr(i))
