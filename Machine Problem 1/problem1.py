"""
Banking System
Check balance 
Deposit Money 
Withdraw Money 
exit the program 
"""

balance = float(input("\nEnter initial balance: "))

def check_balance():
    print(f"Your current balance is {balance}")


def withdraw(amount): 
    global balance
    if amount > balance:
        print(f"Insufficient funds. you cannot withdraw {amount} poor")
    else: 
        balance -= amount
        print(f"You have withdraw {amount} your new balance is {balance}")

def deposit(amount): 
    global balance
    balance += amount
    print(f"You have successfully depositeed {amount} your new balance is {balance}")


while True: 
    print("\nChoose: ")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit\n")

    choice = input("Choose an option: ")

    

    if choice == "1": 
        check_balance()
    elif choice == "2": 
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)
    elif choice == "3": 
        amount = float(input("Enter amount to withdraw: "))
        withdraw(amount)
    elif choice == "4": 
        print("Exiting....")
        break
    else: 
        if choice.isalpha():
            print("Invalid input, Please enter a number")
        else: 
            print("Input is not on the choice please try again")