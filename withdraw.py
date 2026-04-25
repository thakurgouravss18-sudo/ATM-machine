import utils
from datetime import datetime

def withdraw():
    amount = float(input("Enter amount to withdraw: Rs. "))
    if amount <= 0:
        print("Amount must be greater than zero.")
    elif amount % 100 != 0:
        print("Amount must be a multiple of 100.")
    elif amount > utils.balance:
        print(f"Insufficient balance! Available: Rs. {utils.balance:.2f}")
    else:
        utils.balance -= amount
        utils.transactions.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} | WITHDRAW | Rs. {amount:.2f} | Balance: Rs. {utils.balance:.2f}")
        print(f"Withdrawal Successful! Remaining Balance: Rs. {utils.balance:.2f}")
