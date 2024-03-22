#simple if elif else problems
#Convert Uppercase character to Lowercase and vice versa

ch = input("Enter a letter from the Alphabet = ")
if ch>='A' and ch<='Z':
    n=ord(ch)
    n+=32
    ch=chr(n)
    print(ch)
elif ch>='a' and ch<='z':
    n=ord(ch)
    n-=32
    ch=chr(n)
    print(ch)
else:
    print("Invalid input. Try again and enter a valid, single letter to process.")