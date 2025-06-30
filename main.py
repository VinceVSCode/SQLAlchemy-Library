from controllers.user_controller import add_user, list_users
from controllers.author_controller import add_author, list_authors
from controllers.book_controller import add_book, list_books

def main_menu():
    while True:
        print("\n📚 Library CLI Menu")
        print("1. Add User")
        print("2. List Users")
        print("3. Add Author")
        print("4. List Authors")
        print("5. Add Book")
        print("6. List Books")

        print("0. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == "2":
            list_users()
        elif choice == "3":
            name = input("Enter author name: ")
            add_author(name)
        elif choice == "4":
            list_authors()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
