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
