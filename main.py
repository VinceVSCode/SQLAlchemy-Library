from controllers.user_controller import add_user

def main_menu():
    while True:
        print("\n📚 Library Menu")
        print("1. Add User")
        print("2. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == "2":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()
