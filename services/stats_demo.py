# This is a demo service to show how to use the stats service.
from stats import count_books_by_genre, count_books_by_author
from database.database_init import SessionLocal

if __name__ == "__main__":
    count_books_by_author()
    count_books_by_genre()
