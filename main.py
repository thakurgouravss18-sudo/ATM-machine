import utils
from check_balance import check_balance
from withdraw import withdraw
from deposit import deposit
from statement import statement

def atm():
    print("Welcome to Python ATM")

    # PIN check
    attempts = 0
    while attempts < 3:
        entered_pin = input("Enter your PIN: ")
        if entered_pin == utils.pin:
            print(f"PIN Verified. Welcome, {utils.name}!")
            break
        else:
            attempts += 1
            print(f"Wrong PIN. Attempts remaining: {3 - attempts}")
    else:
        print("Too many wrong attempts. Goodbye!")
        return

    # Menu loop
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Statement")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:     check_balance()
        elif choice == 2:   withdraw()
        elif choice == 3:   deposit()
        elif choice == 4:   statement()
        elif choice == 5:
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice")

atm()
