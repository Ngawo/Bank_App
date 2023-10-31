import my_module
from my_module import load_user_accounts, is_valid_username, is_valid_password, create_account, withdraw


def main_menu():
    print("WELCOME TO THE BANK")
    print("1. New account")
    print("2. Login")
    print("3. Exit")


def transaction_menu(username, user_accounts):
    print("Current Balance for {}: R{:.2f}".format(username, user_accounts[username]['balance']))
    print("Would you like to deposit, withdraw, or view transactions?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Transactions")
    print("4. Exit")


# Main program
user_accounts = load_user_accounts()
while True:
    main_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        username = input("Enter your desired username: ").strip().upper()
        if username == "":
            print("Username cannot be empty. Transaction canceled.")
            break

        if not is_valid_username(username):
            print("Invalid username. Please follow the criteria.")
            continue
        if username in user_accounts:
            print("Username already exists. Please choose another username.")
            continue
        user_password = input("Enter your password: ")
        confirm_password = input("Please confirm password: ")
        if user_password != confirm_password:
            print("Password doesn't match or is invalid. Please follow the criteria.")
            if not is_valid_password(user_password):
                print("Password must have only 6 characters")
                continue

        initial_balance_str = input("Enter the initial balance for the new account: R")
        initial_balance_str = initial_balance_str.replace(" ", "")  # Remove spaces
        initial_balance = float(initial_balance_str)
        create_account(user_accounts, username, initial_balance, user_password)
        while True:
            transaction_menu(username, user_accounts)
            transaction_choice = input("Enter your choice: ")
            if transaction_choice == "1":
                try:
                    amount_str = input("How much would you like to deposit? R")
                    amount_str = amount_str.replace(" ", "")  # Remove spaces
                    amount = float(amount_str)
                    my_module.deposit(user_accounts, username, amount)  # calling the function from another module
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif transaction_choice == "2":
                try:
                    amount_str = input("How much would you like to withdraw? R")
                    amount_str = amount_str.replace(" ", "")  # Remove spaces
                    amount = float(amount_str)
                    withdraw(user_accounts, username, amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            else:
                break
    elif choice == "2":
        username = input("Enter your account username: ").strip().upper()
        if username == "":
            print("Username cannot be empty. Transaction canceled.")
            if not is_valid_username(username):
                print("Invalid username. Please follow the criteria.")
                continue
        user_password = input("Enter your password: ")
        if username not in user_accounts or user_accounts[username]['password'] != user_password:
            print("Invalid username or password. Please try again.")
            continue
        while True:
            transaction_menu(username, user_accounts)
            transaction_choice = input("Enter your choice: ")
            if transaction_choice == "1":
                try:
                    amount_str = input("How much would you like to deposit? R")
                    amount_str = amount_str.replace(" ", "")  # Remove spaces
                    amount = float(amount_str)
                    my_module.deposit(user_accounts, username, amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif transaction_choice == "2":
                try:
                    amount_str = input("How much would you like to withdraw? R")
                    amount_str = amount_str.replace(" ", "")  # Remove spaces
                    amount = float(amount_str)
                    withdraw(user_accounts, username, amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif transaction_choice == "3":
                my_module.view_transactions(username)
            elif choice == "4":
                 break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")

print("Thank you for using our Bank Application")
