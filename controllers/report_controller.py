from sqlalchemy import func
from models import Book, Author, Loan, User
from database.database_init import SessionLocal
from typing import Optional
from datetime import datetime,timedelta,timezone

# A function that will count books by their genre
def count_books_by_genre():
    """Count the number of books in each genre.
    Returns a dictionary with genres as keys and their respective book counts as values.
    If no books are found, it returns an empty dictionary.
    """
    # Open a session to the database
    session = SessionLocal()
    
    try:
        genre_counts = session.query(Book.genre, func.count(Book.id)).group_by(Book.genre).all()
        if not genre_counts:
            print("No books found.")
        else:
            print(f"Found {len(genre_counts)} genre(s) with their respective book counts.")
        # Convert the list of tuples to a dictionary
        dict_genre_counts = {genre: count for genre, count in genre_counts}
        return dict_genre_counts
    except Exception as e:
        # Handle any exceptions that occur during the query
        print(f"Error counting books by genre: {e}")
        return {}
    finally:
        session.close()

# A function that will count books by their author
def count_books_by_author():
    """Count the number of books by each author.
    Returns a dictionary with authors as keys and their respective book counts as values.
    If no books are found, it returns an empty dictionary.
    """
    # Open a session to the database
    session = SessionLocal()

    try:
        author_count = (session.query(Author.name,func.count(Book.id))
                        .join(Book)
                        .group_by(Author.name)
                        .all()
        )
        if not author_count:
            print("No books found.")
        else:
            print(f"Found {len(author_count)} author(s) with their respective book counts.")
        # Convert the list of tuples to a dictionary
        dict_author_count = {author: count for author, count in author_count}
        return dict_author_count
    except Exception as e:
        # Handle any exceptions that occur during the query
        print(f"Error counting books by author: {e}")
        return {}
    finally:
        session.close()
    
# A function that will get the most borrowed book, with a limit of 5
def get_most_borrowed_books(limit = 5)-> Optional[list]:
    """Get the most borrowed book.
    Returns the title of the most borrowed book and the number of times it has been borrowed.
    If no books have been borrowed, it returns None.
    """
    session = SessionLocal()

    try:
        most_borrowed = (
            session.query(Book.title,  func.count(Loan.id).label("borrow_count"))
            .join(Loan, Book.id == Loan.book_id)
            .group_by(Book.id)
            .order_by(func.count(Loan.id).desc())
            .limit(limit)
            .all()
        )
        return most_borrowed
    except Exception as e:
        print(f"Error getting most borrowed book: {e}")
        return None
    finally:
        session.close()

# A function that will gather users with no loans
def get_users_with_no_loans():
    """Get users who have no loans.
    Returns a list of User objects who have no associated loans.
    """
    session = SessionLocal()

    try:
        users_with_no_loans = (
            session.query(User)
            .outerjoin(Loan, User.id == Loan.user_id)
            .filter(Loan.id.is_(None))
            .all()
        )
        return users_with_no_loans
    except Exception as e:
        print(f"Error getting users with no loans: {e}")
        return []
    finally:
        session.close()

# A function that will get books that have never been borrowed
def get_books_never_borrowed():
    """Get books that have never been borrowed.
    Returns a list of Book objects that have no associated loans.
    """
    session = SessionLocal()

    try:
        books_never_borrowed = (
            session.query(Book)
            .outerjoin(Loan, Book.id == Loan.book_id)
            .filter(Loan.id.is_(None))
            .all()
        )
        return books_never_borrowed
    except Exception as e:
        print(f"Error getting books never borrowed: {e}")
        return []
    finally:
        session.close()

# A function that will get overdue loans
def get_overdue_loans():
    """Get overdue loans.
    Returns a list of Loan objects that are overdue (not returned and borrowed more than 14 days ago).
    """
    session = SessionLocal()
    try:
        now = datetime.now(timezone.utc)
        overdue_loans = (
            session.query(Loan)
            .filter(Loan.returned_date.is_(None))
            .filter(Loan.borrowed_date + timedelta(days=14) < now)
            .all()
        )
        return overdue_loans
    finally:
        session.close()