# simple if elif else problems
# Choose Deposit or Withdraw option, then complete the transaction
# Use Nested ifs
# Use def

bal = float(input("Enter last known balance in Rupees.ps format = "))
trans_type = input("Enter 'd' or 'D' for Deposit --- 'w' or 'W' for Withdraw -> (d/w) = ")
amt = float(input("Enter Transaction amount in Rupees (multiples of 100 only) = "))


def deposit(balance, amount):
    balance += amount
    print("Deposit Successful.")
    return balance


def withdraw(balance, amount):
    if amount > balance:
        print(f'Insufficient balance.')
        return balance
    elif amount % 100 == 0:
        balance -= amount
        print("Withdrawal Successful.")
        return balance


if amt>=0:
    if amt%100==0:
        if trans_type == 'd' or trans_type == 'D':
            bal = deposit(bal, amt)
        elif trans_type == 'w' or trans_type == 'W':
            bal = withdraw(bal, amt)
        else:
            print("Invalid Transaction type. Use 'd' or 'D' for Deposit --- 'w' or 'W' for Withdraw when you try again.")
    else:
        print("Enter transaction amount in multiples of 100 only.")
else:
    print("Invalid transaction amount. Try again.")
print(f'Your current balance : {bal:.2f}')