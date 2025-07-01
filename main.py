from controllers.report_controller import count_books_by_author, count_books_by_genre, get_most_borrowed_books,get_users_with_no_loans,get_books_never_borrowed,get_overdue_loans
from controllers.user_controller import add_user, list_users
from controllers.author_controller import add_author, list_authors
from controllers.book_controller import add_book, get_books_before_year, get_books_by_author, get_books_by_genre, get_books_by_substring, list_books
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
        print("9. List books by genre")
        print("10. List books by author")
        print("11. List books before a year")
        print("12. List books by title keyword")
        print("13. Show book count by genre")
        print("14. Show book count by author")
        print("15. Show most borrowed books")
        print("16. List users with no loans")
        print("17. Show books that have never been borrowed")
        print("18. Show overdue loans")

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

        elif choice == "9":
            genre = input("Genre: ")
            get_books_by_genre(genre)

        elif choice == "10":
            author = input("Author name: ")
            get_books_by_author(author)

        elif choice == "11":
            year = int(input("Enter year: "))
            get_books_before_year(year)

        elif choice == "12":
            keyword = input("Keyword in title: ")
            get_books_by_substring(keyword)
        elif choice == "13":
            genre_counts = count_books_by_genre()
            for genre, count in genre_counts.items():
                print(f"{genre}: {count} book(s)")

        elif choice == "14":
            author_counts = count_books_by_author()
            for author, count in author_counts.items():
                print(f"{author}: {count} book(s)")

        elif choice == "15":
            count = int(input("How many top books to show? "))
            top_books = get_most_borrowed_books(count)
            if top_books is None:
                print("No borrowed books found.")
            else:
                for title, num in top_books:
                    print(f"{title} — borrowed {num} time(s)")
        elif choice == "16":
            users = get_users_with_no_loans()
            if not users:
                print("Everyone has borrowed something.")
            else:
                for user in users:
                    print(f"📭 {user.name} — {user.email}")
        elif choice == "17":
            books = get_books_never_borrowed()
            if not books:
                print("📚 All books have been borrowed at least once.")
            else:
                print("📕 Never borrowed:")
                for book in books:
                    print(f"- {book.title}")

        elif choice == "18":
            loans = get_overdue_loans()
            if not loans:
                print("🎉 No overdue loans!")
            else:
                print("⚠️ Overdue Loans:")
                for loan in loans:
                    print(f"- {loan.book.title} borrowed by {loan.user.name} on {loan.borrowed_date}")


        elif choice == "0":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
