from controllers.user_controller import add_user, list_users
from controllers.author_controller import add_author, list_authors
from controllers.book_controller import add_book, list_books
from controllers.loan_controller import borrow_book, return_book


def main_menu():
    while True:
        print("\n📚 Library CLI Menu")
        print("1. Add User")
        print("2. List Users")
        print("3. Add Author")
        print("4. List Authors")
        print("5. Add Book")
        print("6. List Books")
        print("7. Borrow Book")
        print("8. Return Book")

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
        elif choice == "5":
            title = input("Book title: ")
            author = input("Author name (must exist): ")
            genre = input("Genre: ")
            year = int(input("Published year: "))
            copies = int(input("Number of copies: "))
            add_book(title, author, genre, year, copies)

        elif choice == "6":
            list_books()
            
        elif choice == "7":
            email = input("User email: ")
            title = input("Book title: ")
            borrow_book(email, title)

        elif choice == "8":
            email = input("User email: ")
            title = input("Book title: ")
            return_book(email, title)

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
