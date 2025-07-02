from fastapi import APIRouter
from database.database_init import SessionLocal
from models.books import Book

router = APIRouter()

@router.get("/books")
def get_books():
    session = SessionLocal()
    try:
        books = session.query(Book).all()
        return books
    finally:
        session.close()
        return [
            {
                "id": book.id, 
                "title": book.title,
                "genre": book.genre, 
                "published_year": book.published_year
            }
            for book in books
        ]