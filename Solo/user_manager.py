#switching on python built in tools
import csv
import os

#creating two empty lists. Every user added will go into these lists
active_users = []
disabled_users = []

#ask for a username and password, put them together in a dictionary, then add that dictionary to the active user list
def add_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = {"username": username, "password": password}
    active_users.append(user)
    print(f"{username} has been added.")

#loop through both lists and print each username to the screen
def view_users():
    print("\nActive Users:")
    for user in active_users:
        print(f"  - {user['username']}")

    print("\nDisabled Users:")
    for user in disabled_users:
        print(f"  - {user['username']}")

#ask for a username, search the active list for it, if found, move that dictionary across to the disabled list
def disable_user():
    username = input("Enter username to disable: ")
    for user in active_users:
        if user["username"] == username:
            active_users.remove(user)
            disabled_users.append(user)
            print(f"{username} has been disabled.")
            return
    print("User not found in active list.")

#(opposite to previous def) find user in the disabled list and move them back to active
def enable_user():
    username = input("Enter username to enable: ")
    for user in disabled_users:
        if user["username"] == username:
            disabled_users.remove(user)
            active_users.append(user)
            print(f"{username} has been enabled.")
            return
    print("User not found in disabled list.")

#ask for username and password, then check every user in the active list to see if both match. If they do, grant access. If the loop finishes without finding a match, access is denied.
def test_login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    for user in active_users:
        if user["username"] == username and user["password"] == password:
            print("ACCESS GRANTED")
            return
    print("ACCESS DENIED")

#open/create "users.csv" and write every from both lists into it. Also, add a status column to know where they belong.
def save_users():
    with open("users.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["username", "password", "status"])
        writer.writeheader()
        for user in active_users:
            writer.writerow({"username": user["username"], "password": user["password"], "status": "active"})
        for user in disabled_users:
            writer.writerow({"username": user["username"], "password": user["password"], "status": "disabled"})

#on startup, check if user.csv exists. If it does, read every row and put each user back into the correct list based on their status column
def load_users():
    if not os.path.exists("users.csv"):
        return
    with open("users.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            user = {"username": row["username"], "password": row["password"]}
            if row["status"] == "active":
                active_users.append(user)
            else:
                disabled_users.append(user)
