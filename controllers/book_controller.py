from database.database_init import SessionLocal
from models import Book, Author, User
from sqlalchemy.orm import joinedload


def add_book(title: str, author_name: str, genre: str, year: int, copies: int = 1):
    session = SessionLocal()
    try:
        author = session.query(Author).filter_by(name=author_name).first()
        if not author:
            print(f"❗ Author '{author_name}' not found.")
            return

        existing = session.query(Book).filter_by(title=title, author_id=author.id).first()
        if existing:
            print(f"❗ Book '{title}' by {author_name} already exists.")
            return

        book = Book(
            title=title,
            author_id=author.id,
            genre=genre,
            published_year=year,
            copies=copies,
            is_available=True  # initially available
        )
        session.add(book)
        session.commit()
        print(f"✅ Book '{title}' added.")
    finally:
        session.close()


def list_books():
    session = SessionLocal()
    try:
        books = session.query(Book).options(joinedload(Book.author)).all()
        if not books:
            print("⚠️ No books found.")
        for book in books:
            status = "Available" if bool(book.is_available) else "Checked out"
            print(f" - {book.title} by {book.author.name} ({book.genre}, {book.published_year}) — {status} [{book.copies} copies]")
    finally:
        session.close()

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
