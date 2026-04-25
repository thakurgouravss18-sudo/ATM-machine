import utils

def statement():
    if len(utils.transactions) == 0:
        print("No transactions found.")
    else:
        print("\n--- Transaction History ---")
        for t in utils.transactions:
            print(t)
