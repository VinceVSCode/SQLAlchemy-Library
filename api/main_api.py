# main_api.py will be the entry point for the FastAPI application.
# It will set up the FastAPI app and include the router from the api.routes module.
# uvicorn api.main_api:app --reload

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from api.routes import router
from fastapi.responses import HTMLResponse
import models,schemas
from database.database_init import engine, get_db

models.Base.metadata.create_all(bind=engine)

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