from sqlalchemy import func
from models import Book, Author
from database.database_init import SessionLocal

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
    