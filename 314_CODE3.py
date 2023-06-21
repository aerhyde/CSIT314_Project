import os

registered_users = {}

def sign_up():
    while True:
        username = input("Create a username: ")
        if username in registered_users:
            print("Username already exists. Please enter a different username.")
        else:
            password = input("Create a password (at least 8 characters): ")
            if len(password) < 8:
                print("Password should be at least 8 characters long.")
            else:
                registered_users[username] = password
                print("Sign up successful!")
                break

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in registered_users and registered_users[username] == password:
        print("Login successful!")

        while True:
            print("Options:")
            print("1. Send a message")
            print("2. Create a text file")
            print("3. View a text file")
            print("4. Edit a text file")
            print("5. Logout")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                send_message(username)
            elif choice == "2":
                create_text_file()
            elif choice == "3":
                view_text_file()
            elif choice == "4":
                edit_text_file()
            elif choice == "5":
                print("Logged out.")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

    else:
        print("Wrong username or password.")

def send_message(sender):
    recipient = input("Enter the username of the recipient: ")
    if recipient != sender and recipient in registered_users:
        message = input("Enter your message: ")
        if message.strip() != "":
            print("Message sent successfully!")
        else:
            print("Message cannot be blank.")
    else:
        print("Invalid recipient username.")

def create_text_file():
    filename = input("Enter the submission title: ")
    content = input("Enter the file content: ")
    filename = filename.strip()

    if filename != "":
        filename += ".txt"
        with open(filename, "w") as file:
            file.write(content)
        print("File created successfully!")
    else:
        print("Invalid file name.")

def view_text_file():
    filename = input("Enter the file name to view: ")
    filename = filename.strip()

    if filename != "":
        filename += ".txt"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                content = file.read()
            print("File content:")
            print(content)
        else:
            print("File not found.")
    else:
        print("Invalid file name.")

def edit_text_file():
    filename = input("Enter the file name to edit: ")
    filename = filename.strip()

    if filename != "":
        filename += ".txt"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                content = file.read()
            print("Current file content:")
            print(content)

            new_content = input("Enter the new content: ")
            with open(filename, "w") as file:
                file.write(new_content)
            print("File edited successfully!")
        else:
            print("File not found.")
    else:
        print("Invalid file name.")

while True:
    print("Menu:")
    print("1. Sign up")
    print("2. Login")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        sign_up()
    elif choice == "2":
        login()
    else:
        print("Invalid choice. Please enter 1 or 2.")

    print()