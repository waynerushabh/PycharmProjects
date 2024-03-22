#simple if elif else problems
# Char input is a letter or number or special character

ch = input("Enter the character to check ( Only single key input allowed ) = ")

if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
    print(f'{ch} is a letter from the alphabet.')
elif '0' <= ch <= '9':
    print(f'{ch} is a number between 0-9.')
elif 0 <= ord(ch) <= 127:
    print(f'{ch} might be a special character or punctuation or a valid ASCII/Unicode character.')
else:
    print(f'{ch} : not a valid input/unrecognisable character. Character should be single and ASCII/Unicode compliant.')