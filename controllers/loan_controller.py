from database.database_init import SessionLocal
from models import Loan, Book, User
from datetime import datetime, timezone
from sqlalchemy.orm import joinedload


def borrow_book(user_email: str, book_title: str):
    session = SessionLocal()
    try:
        user = session.query(User).filter_by(email=user_email).first()
        book = session.query(Book).filter_by(title=book_title).first()

        if not user:
            print(f"❗ User '{user_email}' not found.")
            return
        if not book:
            print(f"❗ Book '{book_title}' not found.")
            return
        if not bool(book.is_available) or book.copies <= 0:
            print(f"❌ Book '{book.title}' is currently not available.")
            return

        loan = Loan(book_id=book.id, user_id=user.id, borrowed_date=datetime.now())
        session.add(loan)

        book.copies -= 1
        book.is_available = book.copies > 0
        session.commit()

        print(f"✅ '{book.title}' borrowed by {user.username}.")
    finally:
        session.close()


def return_book(user_email: str, book_title: str):
    session = SessionLocal()
    try:
        user = session.query(User).filter_by(email=user_email).first()
        book = session.query(Book).filter_by(title=book_title).first()

        if not user or not book:
            print("❌ Invalid user or book.")
            return

        loan = (
            session.query(Loan)
            .filter_by(user_id=user.id, book_id=book.id, returned_date=None)
            .first()
        )

        if not loan:
            print(f"❌ No active loan found for '{book_title}' by {user.username}.")
            return

        # Mark the loan as returned
        setattr(loan, "returned_date",datetime.now(timezone.utc))
        book.copies += 1
        setattr(book, "is_available", True)
        session.commit()

        print(f"✅ '{book.title}' returned by {user.username}.")
    finally:
        session.close()

# Create a function to get all loaned books with their users
def get_borrowed_books_with_users():
    session = SessionLocal()
    try:
        # The thought process is Loan -> Book and Loan -> User
        borrowed_books = (session.query(Loan)
            .options(joinedload(Loan.book),joinedload(Loan.user))
            .filter(Loan.returned == None)
            .all()
        )
        return borrowed_books
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        session.close()

def get_users_and_their_books():
    session =  SessionLocal()
    try:
        users = (
            session.query(User)
            .options(joinedload(User.loan).joinedload(Loan.book))
            .all()
        )
        return users
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        session.close()
