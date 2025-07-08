# api/routes.py
# This file defines the routes for the FastAPI application.
# It will handle requests related to books, such as retrieving a list of books.

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database_init import SessionLocal
from models import Book, User , Loan


router = APIRouter()

# Root endpoint for the API
# This will return a welcome message when the root URL is accessed.
# @router.get("/")
# def read_root():
#     return {"message": "Welcome to the Library API!"}

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

# Get a list of all users
@router.get("/users" )
def get_users(db: Session = Depends(get_db)):

    """
    Get a list of all users.
    This endpoint retrieves all users from the database.
    """
    try:
        users = db.query(User).all()
        return [
            {
                "id": user.id,
                "name": user.username,
                "email": user.email
            }
            for user in users
        ]
    except Exception as e:
        return {"error": str(e)}

# Get loans 
@router.get("/loans")
def get_active_loans(db: Session = Depends(get_db)):
    """
    Get a list of all loans.
    This endpoint retrieves all loans from the database.
    """
    try:
        loans = db.query(Loan).filter(Loan.return_date.is_(None)).all()
        if not loans:
            return {"message": "No active loans found."}
        # Return a list of loans with relevant details
        results = []
        for loan in loans:
            results.append({
            "loan_id": loan.id,
            "book_title": loan.book.title,
            "borrowed_by": loan.user.name,
            "borrowed_date": loan.borrowed_date.isoformat()
            })
        return results
    except Exception as e:
        return {"error": str(e)}



