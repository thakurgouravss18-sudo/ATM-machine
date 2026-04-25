import utils
from datetime import datetime

def deposit():
    amount = float(input("Enter amount to deposit: Rs. "))
    if amount <= 0:
        print("Amount must be greater than zero.")
    else:
        utils.balance += amount
        utils.transactions.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} | DEPOSIT  | Rs. {amount:.2f} | Balance: Rs. {utils.balance:.2f}")
        print(f"Deposit Successful! New Balance: Rs. {utils.balance:.2f}")
