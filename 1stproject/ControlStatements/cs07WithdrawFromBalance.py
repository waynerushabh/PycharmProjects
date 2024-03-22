#simple if elif else problems

tamt = int(input("Enter Transaction Amount = "))
bal = float(input("Enter Last Known Balance = "))
if tamt>0 and tamt%5==0 and (tamt+0.50)<bal and bal>0:
    bal=bal-(tamt+0.50)
    print(f'Balance after Transaction = {bal:.2f}')
elif tamt%5!=0:
    print(f'Error in transaction. Transactions should be in multiples of 5. Balance = {bal:.2f}')
elif (tamt+0.50>bal):
    print(f'Error in transaction. Transaction Amount exceeds the limit. Balance = {bal:.2f}')
else:
    print(f'Transaction Failed : Unknown Error. Please Try Again.')