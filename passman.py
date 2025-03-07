import hashlib
import getpass

password_manager = {}

def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login to an existing account, or 0 to exit the application: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid choice, please select again")