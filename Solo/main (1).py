#import everything from user_manager.py
from user_manager import (
    active_users, disabled_users,
    add_user, view_users, disable_user, enable_user,
    test_login, save_users, load_users
)
#load saved users from CSV before menu appears
load_users()

#a loop that keeps showing the menu and witing for input until the user chooses to exit
while True:
    print("\n=== User Management System ===")
    print("1. Add user")
    print("2. View users")
    print("3. Disable a user")
    print("4. Enable a user")
    print("5. Test login")
    print("0. Exit")

    choice = input("Choose an option: ")
#each "if" block calls the relevant function. Any option that changes the data also calls "save_users()" straight so the CSV is updated.
    if choice == "1":
        add_user()
        save_users()
    elif choice == "2":
        view_users()
    elif choice == "3":
        disable_user()
        save_users()
    elif choice == "4":
        enable_user()
        save_users()
    elif choice == "5":
        test_login()
    #exit the "while true" loop, ending the program using "break"
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")
