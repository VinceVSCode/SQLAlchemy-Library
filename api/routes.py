# api/routes.py
# This file defines the routes for the FastAPI application.
# It will handle requests related to books, such as retrieving a list of books.

from fastapi import APIRouter, Depends
from database.database_init import SessionLocal
from models.books import Book

router = APIRouter()

# Root endpoint for the API
# This will return a welcome message when the root URL is accessed.
@router.get("/")
def read_root():
    return {"message": "Welcome to the Library API!"}

# Get a list of all books
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

# Dependency for injecting a new database into each request
def get_db():
    """
    Dependency to get a database session.
    This will be used in the route handlers to interact with the database.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
