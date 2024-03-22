# wap to count number of vowels in a given string
# str1 = input("Enter any string = ")
# c = 0
# for ch in str1:
#     if ch in "aeiouAEIOU":
#         c += 1
# print(f'No. of vowels in string = {c}')

# wap to find given string pal or not
# str1 = input("Enter any string = ")
# if str1 == str1[::-1]:
#     print("String is a palindrome.")
# else:
#     print("String is not a palindrome.")

# # wap to count frequency of characters
# str1 = input("Enter any string = ")
# # # set_of_chars = set(str1)
# # # str2 = ""
# dict_of_chars = {}
# # # print("{", end='')
# for ch in str1:
#     c = str1.count(ch)
#     dict_of_chars[ch] = c
# print(dict_of_chars)
# # print(str2, "}", end='')
# print()

# # wap to convert string to uppercase
# str1 = input("Enter Any String = ")
# str2 = ""
# for ch in str1:
#     if 'a' <= ch <= 'z':
#         ch = chr(ord(ch)-32)
#         str2 += ch
#     else:
#         str2 += ch
# print(f'String in uppercase = {str2}')
# print()

# # wap to capitalize string
# str1 = input("Enter any String = ")
# str2 = ""
# i = 0
# while i < len(str1):
#     if i == 0:
#         if 'a' <= str1[i] <= 'z':
#             str2 += chr(ord(str1[i])-32)
#         else:
#             str2 += str1[i]
#     elif str1[i] == ' ':
#         while str1[i] == ' ':
#             str2 += str1[i]
#             i += 1
#             if 'a' <= str1[i] <= 'z':
#                 str2 += chr(ord(str1[i])-32)
#             else:
#                 str2 += str1[i]
#     elif 'A' <= str1[i] <= 'Z':
#         str2 += chr(ord(str1[i])+32)
#     else:
#         str2 += str1[i]
#     i += 1
#
# print(str1)
# print(str2)

