from models import Book, Loan, User
from database.database_init import SessionLocal
from datetime import datetime

# Function to borrow a book
def borrow_book(user_id: int, book_id: int):
    session = SessionLocal()
    try:
        book = session.query(Book).get(book_id)
        user = session.query(User).get(user_id)

        if not book or not user:
            print("❌ Book or user not found.")
            return

        if book.available_copies < 1:
            print("❌ No available copies.")
            return

        loan = Loan(user=user, book=book, borrowed_date=datetime.utcnow())
        session.add(loan)
        session.commit()
        print(f"✅ {user.name} borrowed '{book.title}'.")
    except Exception as e:
        session.rollback()
        print("❌ Error during borrowing:", e)
    finally:
        session.close()

# Function to return a book
def return_book(loan_id: int):
    session = SessionLocal()
    try:
        loan = session.query(Loan).get(loan_id)
        if loan is None or loan.returned_date is not None:
            print("❌ Invalid loan or already returned.")
            return

        loan.returned_date = datetime.utcnow()
        session.commit()
        print(f"✅ Returned '{loan.book.title}' from {loan.user.name}.")
    except Exception as e:
        session.rollback()
        print("❌ Error during return:", e)
    finally:
        session.close()

# List all borrowed books
def list_borrowed_books():
    session = SessionLocal()
    try:
        loans = session.query(Loan).filter(Loan.returned_date == None).all()
        if not loans:
            print("📕 No borrowed books.")
            return

        print("📕 Borrowed books:")
        for loan in loans:
            print(f" - {loan.book.title} borrowed by {loan.user.name} on {loan.borrowed_date}")
    except Exception as e:
        print("❌ Error listing borrowed books:", e)
    finally:
        session.close()