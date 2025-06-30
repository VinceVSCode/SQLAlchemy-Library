from database.database_init import SessionLocal
from models import Loan, Book, User
from datetime import datetime, timezone


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

        print(f"✅ '{book.title}' borrowed by {user.name}.")
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
            print(f"❌ No active loan found for '{book_title}' by {user.name}.")
            return

        # Mark the loan as returned
        setattr(loan, "returned_date",datetime.now(timezone.utc))
        book.copies += 1
        setattr(book, "is_available", True)
        session.commit()

        print(f"✅ '{book.title}' returned by {user.name}.")
    finally:
        session.close()
