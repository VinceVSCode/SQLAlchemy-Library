from database.database_init import SessionLocal
from models import Book, Loan, User
from sqlalchemy.orm import joinedload

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

