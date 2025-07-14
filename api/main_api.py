# main_api.py will be the entry point for the FastAPI application.
# It will set up the FastAPI app and include the router from the api.routes module.
# uvicorn api.main_api:app --reload

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import hashlib
from datetime import datetime, timezone
now = datetime.now(timezone.utc)

from api.routes import router
from fastapi.responses import HTMLResponse
import schemas
import models
from models.users import User
from models.base import Base
from models.books import Book
from models.loans import Loan
from models.authors import Author
# Import the database engine and session dependency


from database.database_init import engine, get_db

try:
    models.Base.metadata.create_all(bind=engine)
except Exception as e:
    print(f"❌ DB Table Creation Failed: {e}")

# Create the FastAPI application instance
app = FastAPI()

# Include the router from the api.routes module
# This will register all the routes defined in the router with the FastAPI app.
app.include_router(router)

@app.get("/", response_class=HTMLResponse  )
def root_menu():
    """
    Root endpoint that returns a simple HTML response.
    This can be used to provide a welcome message or a simple UI.
    """
    return """
    <html>
        <head>
            <title>Library API Menu</title>
        </head>
        <body>
            <h1>Welcome to the Library API!</h1>
            <p>Use the endpoints to interact with the library system.</p>
            <ul>
                <li><a href="/docs">Swagger UI </a></li>
                <li><a href="/books">View all books</a></li>
                <li><a href="/users">View all users</a></li>
                <li><a href="/loans">View active loans</a></li>
            </ul>
            
        </body>
    </html>
    """
# ------------ Book management endpoints --------------
# Create a new book
@app.post("/books/", response_model=schemas.BookOut)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """
    Create a new book in the library.
    """
    new_book = models.Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

# Read list of all books
@app.get("/books/",response_model=list[schemas.BookOut])
def read_books(db: Session = Depends(get_db)):
    """
    Retrieve a list of all books in the library.
    """
    books = db.query(models.Book).all()
    return books

# READ a single book by ID
@app.get("/books/{book_id}", response_model=schemas.BookOut)
def read_book(book_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a book by its ID.
    """
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# UPDATE a book by ID
@app.put("/books/{book_id}", response_model=schemas.BookOut)
def update_book(book_id: int, updated: schemas.BookUpdate, db: Session = Depends(get_db)):
    """
    Update a book's details by its ID.
    """
    book = db.query(models.Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    for field, value in updated.dict().items():
        setattr(book, field, value)
    db.commit()
    db.refresh(book)
    return book

# DELETE a book by ID
@app.delete("/books/{book_id}", response_model=schemas.BookOut)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Delete a book by its ID.
    """
    book = db.query(models.Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return book

# --------USER management endpoints. --------------(Make more modular later...)
@app.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user in the library system.
    """
    # Check if the user already exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # Create a new user instance with hashed password and add it to the database
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    new_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get All Users
@app.get("/users/", response_model=list[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):
    """
    Retrieve a list of all users in the library system.
    """
    users = db.query(User).all()
    return users

# UPDATE user by ID
@app.put("/users/{user_id}", response_model = schemas.UserOut)
def update_user(user_id: int, updated: schemas.UserUpdate , db: Session = Depends(get_db)):
    """
    Update a user's details by their ID.
    """
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    for field, value in updated.model_dump(exclude_unset=True).items():
        setattr(user, field, value)
    
    db.commit()
    db.refresh(user)
    return user

# DELETE user by ID
@app.delete("/users/{user_id}", response_model=schemas.UserOut)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Delete a user by their ID.
    """
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return user

# ----- Author Endpoints -----

@app.post("/authors/", response_model=schemas.AuthorOut)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Author).filter(models.Author.name == author.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Author already exists")
    new_author = models.Author(name=author.name)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author


@app.get("/authors/", response_model=list[schemas.AuthorOut])
def read_authors(db: Session = Depends(get_db)):
    return db.query(models.Author).all()


# ----- Loan Endpoints -----

@app.post("/loans/borrow", response_model=schemas.LoanOut)
def borrow_book_api(loan: schemas.LoanCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).get(loan.user_id)
    book = db.query(models.Book).get(loan.book_id)
    if not user or not book:
        raise HTTPException(status_code=404, detail="User or book not found")
    if not bool(book.is_available):
        raise HTTPException(status_code=400, detail="Book not available")
    new_loan = models.Loan(book_id=book.id, user_id=user.id)
    db.add(new_loan)
    book.is_available = False
    db.commit()
    db.refresh(new_loan)
    return new_loan


@app.post("/loans/return", response_model=schemas.LoanOut)
def return_book_api(loan: schemas.LoanCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).get(loan.user_id)
    book = db.query(models.Book).get(loan.book_id)
    if not user or not book:
        raise HTTPException(status_code=404, detail="User or book not found")
    db_loan = (
        db.query(models.Loan)
        .filter(
            models.Loan.book_id == book.id,
            models.Loan.user_id == user.id,
            models.Loan.returned_date == None,
        )
        .first()
    )
    if not db_loan:
        raise HTTPException(status_code=404, detail="Active loan not found")
    setattr(db_loan, "returned_date", datetime.now(timezone.utc))
    book.is_available = True
    db.commit()
    db.refresh(db_loan)
    return db_loan