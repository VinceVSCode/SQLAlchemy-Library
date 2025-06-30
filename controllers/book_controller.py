from database.database_init import SessionLocal
from models import Book, Author
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
