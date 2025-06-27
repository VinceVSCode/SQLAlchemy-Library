from models import Book, Loan, User
from database.database_init import SessionLocal
from sqlalchemy.orm import joinedload

def get_books_by_genre(genre: str):
    """Fetch all books of a specific genre."""
    session = SessionLocal()
    try:
        books = session.query(Book).filter(Book.genre == genre).all()
        if not books:
            print(f"No books found in the genre: {genre}")
        else:
            print(f"Found {len(books)} book(s) in the genre: {genre}")
        return books
    except Exception as e:
        print(f"Error fetching books: {e}")
        return []
    finally:
        session.close()

def get_books_before_year(year: int):
    """Fetch all books published before a specific year."""
    session = SessionLocal()
    try:
        books = session.query(Book).filter(Book.published_year < year).all()
        if not books:
            print(f"No books found published before the year: {year}")
        else:
            print(f"Found {len(books)} book(s) published before the year: {year}")
        return books
    except Exception as e:
        print(f"Error fetching books: {e}")
        return []
    finally:
        session.close()

def get_users_with_email_domain(domain: str):
    """Fetch all users with a specific email domain."""
    session = SessionLocal()
    if not domain.startswith('@'):
        print("Please provide a valid email domain starting with '@'.")
        return []
    try:
        pattersn = f"%{domain}"
        users = session.query(User).filter(User.email.like(pattersn)).all()
        if not users:
            print(f"No users found with the email domain: {domain}")
        else:
            print(f"Found {len(users)} user(s) with the email domain: {domain}")
        return users
    except Exception as e:
        print(f"Error fetching users: {e}")
        return []
    finally:
        session.close()

def get_books_by_author(author_name: str):
    """Fetch all books by a specific author."""
    session = SessionLocal()
    try:
        books = (
            session.query(Book)
            .join(Book.author)
            .filter(Book.author.name.ilike(f"%{author_name}%"))
            .options(joinedload(Book.author)) #faster access
            .all()
        )
        if not books:
            print(f"No books found by the author: {author_name}")
        else:
            print(f"Found {len(books)} book(s) by the author: {author_name}")
        return books
    except Exception as e:
        print(f"Error fetching books: {e}")
        return []
    finally:
        session.close()

def get_books_by_substring(substring: str):
    """Fetch all books with a specific substring."""
    session = SessionLocal()
    try:
        books = session.query(Book).filter(Book.title.ilike(f"%{substring}%")).all()
        if not books:
            print(f"No books found with the substring: {substring}")
        else:
            print(f"Found {len(books)} book(s) with the substring: {substring}")
        return books
    except Exception as e:
        print(f"Error fetching books: {e}")
        return []
    finally:
        session.close()