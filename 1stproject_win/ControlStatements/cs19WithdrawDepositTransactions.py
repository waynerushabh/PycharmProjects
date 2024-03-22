# simple if elif else problems
# Choose Deposit or Withdraw option, then complete the transaction
# Use Nested ifs

bal = float(input("Enter last known balance in Rupees.ps format = "))
trans_type = input("Enter 'd' or 'D' for Deposit --- 'w' or 'W' for Withdraw -> (d/w) = ")
amt = float(input("Enter Transaction amount in Rupees (multiples of 100 only) = "))
if trans_type=='d' or trans_type=='D':
    if amt%100==0:
        bal+=amt
        print("Deposit Successful.")
    else:
        print("Enter transaction amount in multiples of 100 only.")
elif trans_type=='w' or trans_type=='W':
    if amt>bal:
        print(f'Insufficient balance. -> {bal:.2f}')
    elif amt%100==0:
        bal-=amt
        print("Withdrawl Successful.")
    else:
        print("Enter transaction amount in multiples of 100 only.")
else:
    print("Invalid Transaction type. Use 'd' or 'D' for Deposit --- 'w' or 'W' for Withdraw when you try again.")
print(f'Your current balance : {bal:.2f}')